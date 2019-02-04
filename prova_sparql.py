import rdflib

#------ ex 1
#g=rdflib.Graph()
#g.load('http://dbpedia.org/resource/Semantic_Web')
#for s,p,o in g:
#    print (s,p,o)


#------ ex 2: examples/prepared_query.py
"""
SPARQL Queries be prepared (i.e parsed and translated to SPARQL algebra)
by the :meth:`rdflib.plugins.sparql.prepareQuery` method.
When executing, variables can be bound with the
``initBindings`` keyword parameter
"""
# from rdflib.plugins.sparql import prepareQuery
# from rdflib.namespace import FOAF
#
# if __name__ == '__main__':
#
#     q = prepareQuery(
#         'SELECT ?s WHERE { ?person foaf:knows ?s .}',
#         initNs={"foaf": FOAF})
#
#     g = rdflib.Graph()
#     g.load("foaf.rdf")
#
#     tim = rdflib.URIRef("http://www.w3.org/People/Berners-Lee/card#i")
#
#     for row in g.query(q, initBindings={'person': tim}):
#         print("--")
#         print(row)

#------ ex 3: examples/simple_example.py
#
# from rdflib import Graph, Literal, BNode, RDF
# from rdflib.namespace import FOAF, DC
#
# if __name__ == '__main__':
#
#     store = Graph()
#
#     # Bind a few prefix, namespace pairs for pretty output
#     store.bind("dc", DC)
#     store.bind("foaf", FOAF)
#
#     # Create an identifier to use as the subject for Donna.
#     donna = BNode()
#
#     # Add triples using store's add method.
#     store.add((donna, RDF.type, FOAF.Person))
#     store.add((donna, FOAF.nick, Literal("donna", lang="foo")))
#     store.add((donna, FOAF.name, Literal("Donna Fales")))
#
#     # Iterate over triples in store and print them out.
#     print("--- printing raw triples ---")
#     for s, p, o in store:
#         print(s, p, o)
#
#     # For each foaf:Person in the store print out its mbox property.
#     print("--- printing mboxes ---")
#     for person in store.subjects(RDF.type, FOAF["Person"]):
#         for mbox in store.objects(person, FOAF["mbox"]):
#             print(mbox)
#
#     # Serialize the store as RDF/XML to the file donna_foaf.rdf.
#     store.serialize("donna_foaf.rdf", format="pretty-xml", max_depth=3)
#
#     # Let's show off the serializers
#
#     print("RDF Serializations:")
#
#     # Serialize as XML
#     print("--- start: rdf-xml ---")
#     print(store.serialize(format="pretty-xml"))
#     print("--- end: rdf-xml ---\n")
#
#     # Serialize as Turtle
#     #print("--- start: turtle ---")
#     #print(store.serialize(format="turtle"))
#     #print("--- end: turtle ---\n")
#
#     # Serialize as NTriples
#     #print("--- start: ntriples ---")
#     #print(store.serialize(format="nt"))
#     #print("--- end: ntriples ---\n")

#------ ex 4: examples/sparql_update_example.py
"""
SPARQL Update statements can be applied with :meth:`rdflib.graph.Graph.update`
"""
# import rdflib
#
# if __name__ == '__main__':
#
#     g = rdflib.Graph()
#     g.load("foaf.rdf")
#
#     g.update('''
#     PREFIX foaf: <http://xmlns.com/foaf/0.1/>
#     PREFIX dbpedia: <http://dbpedia.org/resource/>
#     INSERT
#         { ?s a dbpedia:Human . }
#     WHERE
#         { ?s a foaf:Person . }
#     ''')
#
#     for x in g.subjects(
#             rdflib.RDF.type, rdflib.URIRef('http://dbpedia.org/resource/Human')):
#         print(x)


#------ ex 5: examples/sparqlstore_example.py
"""
A simple example showing how to use the SPARQLStore
"""

# from rdflib import Graph, URIRef, Namespace
#
# if __name__ == '__main__':
#
#     dbo = Namespace('http://dbpedia.org/ontology/')
#
#     graph = Graph('SPARQLStore', identifier="http://dbpedia.org")
#
#     graph.open("http://dbpedia.org/sparql")
#
#     pop = graph.value(
#         URIRef("http://dbpedia.org/resource/Berlin"),
#         dbo.populationTotal)
#
#     print(graph.store.queryString)
#
#     print("According to DBPedia Berlin has a population of", pop)



#------ ex 6: examples/sparql_query_example.py
"""
SPARQL Query using :meth:`rdflib.graph.Graph.query`
The method returns a :class:`~rdflib.query.Result`, iterating over
this yields :class:`~rdflib.query.ResultRow` objects
The variable bindings can be access as attributes of the row objects
For variable names that are not valid python identifiers, dict access
(i.e. with ``row[var] / __getitem__``) is also possible.
:attr:`~rdflib.query.ResultRow.vars` contains the variables
"""
# import rdflib
#
# if __name__ == '__main__':
#
#     g = rdflib.Graph()
#     g.load("foaf.rdf")
#
#     # the QueryProcessor knows the FOAF prefix from the graph
#     # which in turn knows it from reading the RDF/XML file
#     for row in g.query(
#             'select ?s where { [] foaf:knows ?s .}'):
#         print(row.s)
#         # or row["s"]
#         # or row[rdflib.Variable("s")]
#

#--------- altro esempio
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX dbpedia: <http://dbpedia.org/resource/>
    SELECT ?s ?p
    WHERE { ?s ?p dbpedia:Berlin_Berlin } LIMIT 5
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

print("subject and predicate of all triples with object == dbpedia:Berlin_Berlin")

for result in results["results"]["bindings"]:
    print("s=" + result["s"]["value"] + "\tp=" + result["p"]["value"])

print("\nloop over all subjects returned in first query:")
for result in results["results"]["bindings"]:
    sparql.setQuery("""
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX dbpedia: <http://dbpedia.org/resource/>
        SELECT ?p ?o
        WHERE { <""" + result["s"]["value"] +
          """> ?p ?o } LIMIT 10""")
    results2 = sparql.query().convert()
    for result2 in results2["results"]["bindings"]:
        print("p=" + result2["p"]["value"] + "\to=" + result2["o"]["value"])