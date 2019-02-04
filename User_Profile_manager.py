import random
import string
import cherrypy
import json
from pymongo import MongoClient


"""json
{
    'visitatore': {
        'id_visitatore': 'CarlaC',
        'opere': [
            {'opera': {
                'id_opera': 'Cat.8888',
                'tempo_impiegato': 98,
                'apprezzamento': 1,
                'info_ricevute': 1 }
            }
        ]
    }
}
"""

def mongoDBManager(new_entry):

    print("\n- Nuovo VISITATORE arrivato (da Client): " )
    print(str(new_entry))
    print("------------------------------\n")

    vis_id = new_entry['visitatore']['id_visitatore']
    op_id = new_entry['visitatore']['opere'][0]['opera']['id_opera']
    opera = new_entry["visitatore"]["opere"][0]

    #Open the connection with mongo
    client = MongoClient('localhost', 27017)

    #Take the db where I want to save the data
    db = client['visitorProfileDB']  # CREO UN NUOVO DB

    #Take the collection in which I want to put the documents
    visitor_profiles = db.visitorProfiles

    found = 0
    for visit in visitor_profiles.find({'visitatore.id_visitatore': vis_id}):
        # se uguale, fai check opera
        # NB: entra qui dentro solo se lo trova!!!
        found = 1
        resF=visitor_profiles.update(
            {'visitatore.id_visitatore': vis_id},
            {"$addToSet": {'visitatore.opere': opera}})
        print(resF)

        if (resF['nModified']==0):
            print("OPERA GIA VISTA DAL VISITATORE")

        if (resF['nModified']==1):
            print("NUOVA OPERA SALVATA CON SUCCESSO")

    if (found == 0):
        # THIS MEANS THAT IS A NEW VISITOR ARRIVED
        print(found)
        # se il visitor non è nel db significa che dobbiamo aggiungerlo
        jNewEntry = json.dumps(new_entry)
        resU = visitor_profiles.insert_one(new_entry)
        print(resU)
        print("NUOVO VISITATORE SALVATO CON SUCCESSO")


@cherrypy.expose
class UpdateDatabaseWebService(object):

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return cherrypy.session['mystring']

    def POST(self):
        cl = cherrypy.request.headers['Content-Length']
        jData = cherrypy.request.body.read(int(cl))
        rawData = json.loads(jData)
        print("\n- POST RICEVUTA DA CLIENT (json): " + str(jData))

        mongoDBManager(rawData)

        #id_visitatore = rawData['visitatore']['id_visitatore']
        #id_opera = rawData['visitatore']['opere'][0]['opera']['id_opera']
        #print(id_visitatore)
        #print(id_opera)

        return "INVIO DATI EFFETTUATO CON SUCCESSO"

    def PUT(self, another_string):
        cherrypy.session['mystring'] = another_string

    def DELETE(self):
        cherrypy.session.pop('mystring', None)


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        }
    }
    #cherrypy.quickstart(StringGeneratorWebService(), '/', conf)

    #fare configfile
    cherrypy.tree.mount(UpdateDatabaseWebService(), '/', conf)
    cherrypy.config.update("server_UPM.conf")       #port
    cherrypy.engine.start()
    cherrypy.engine.block()


