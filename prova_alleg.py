
#------- test
"""
TEST
"""""
# from franz.openrdf.connect import ag_connect
# with ag_connect('repo', host='192.168.1.130', port='10035',
#                 user='carla', password='coroncina') as conn:
#     print (conn.size())
#

#-------- tut1
"""
Firstly, we will extract the location of the AG server from environment variables.
AllegroGraph connection functions use these environment variables as defaults,
but we will pass the values explicitly to illustrate how to specify connection parameters in Python.
"""""
import os

#AGRAPH_HOST = os.environ.get('AGRAPH_HOST')
AGRAPH_HOST = '192.168.1.130'
AGRAPH_PORT = int(os.environ.get('AGRAPH_PORT', '10035'))
#AGRAPH_USER = os.environ.get('AGRAPH_USER')
AGRAPH_USER = 'carla'
#AGRAPH_PASSWORD = os.environ.get('AGRAPH_PASSWORD')
AGRAPH_PASSWORD = 'coroncina'

"""
The example first connects to an AllegroGraph Server by providing the endpoint (host IP address and port number)
of an already-launched AllegroGraph server.
This creates a client-side server object, which can access the AllegroGraph server’s list of available catalogs
through the listCatalogs() method. Note that the name of the root catalog will be represented by None:
"""
from franz.openrdf.sail.allegrographserver import AllegroGraphServer

print("Connecting to AllegroGraph server --",
      "host:'%s' port:%s" % (AGRAPH_HOST, AGRAPH_PORT))

server = AllegroGraphServer(AGRAPH_HOST, AGRAPH_PORT,
                            AGRAPH_USER, AGRAPH_PASSWORD)
print("Available catalogs:")
for cat_name in server.listCatalogs():
    if cat_name is None:
        print('  - <root catalog>')
    else:
        print('  - ' + str(cat_name))

#------ LISTING REPOSITORY
"""
In the next part of this example, we use the openCatalog() method to create a client-side catalog object.
In this example we will connect to the root catalog. When we look inside that catalog,
we can see which repositories are available:
"""
catalog = server.openCatalog('')
print("Available repositories in catalog '%s':" % catalog.getName())
for repo_name in catalog.listRepositories():
    print('  - ' + repo_name)

#------- CREATING REPOSITORY
"""
The next step is to create a client-side repository object representing the respository we wish to open,
by calling the getRepository() method of the catalog object.
We have to provide the name of the desired repository ('python-tutorial'), and select one of four access modes:

- Repository.RENEW clears the contents of an existing repository before opening. If the indicated repository does not exist, it creates one.
- Repository.OPEN opens an existing repository, or throws an exception if the repository is not found.
- Repository.ACCESS opens an existing repository, or creates a new one if the repository is not found.
- Repository.CREATE creates a new repository, or throws an exception if one by that name already exists.

A new or renewed repository must be initialized, using the initialize() method of the repository object.

"""
from franz.openrdf.repository.repository import Repository

mode = Repository.RENEW
my_repository = catalog.getRepository('python-tutorial', mode)
my_repository.initialize()


#------- CONNECTING TO A REPOSITORY
"""
The goal of all this object-building has been to create a client-side connection object,
whose methods let us manipulate the triples of the repository. The repository object’s getConnection()
method returns this connection object.
"""
conn = my_repository.getConnection()
print('Repository %s is up!' % my_repository.getDatabaseName())
print('It contains %d statement(s).' % conn.size())


#------ Managing indices