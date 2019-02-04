import random
import string
import cherrypy
import json
import os

@cherrypy.expose
class AllegroDB_Support_WebService(object):

    @cherrypy.tools.accept(media='text/plain')
    def GET(self, *uri, **params):

        # apro il config_file suo, prendo ip e porta di dove collegarmi
        try:
            file_hash = open("hash_table_sensorID_artworkID", "r")
            sens_art_dict = json.loads(file_hash.read())
            file_hash.close()
        except:
            raise KeyError("***** ERROR IN READING HASH TABLE JSON FILE *****")

        if uri[0]=="artworkDB_key":
            #prendo valore effettivo del sensorID
            artworkID_rx = params.get('artworkID')
            print("\n- RECEIVED ARTWORK ID is: "+str(artworkID_rx))

            ## qui andrò a gestirmi l'accesso e i dati

            dati_letti_da_db = "HO LETTO DATI DAL GRAPH DB"

        return dati_letti_da_db

if __name__ == '__main__':

    #mi connetto ad allegrograph
    AGRAPH_HOST = '192.168.1.130'
    AGRAPH_PORT = int(os.environ.get('AGRAPH_PORT', '10035'))
    AGRAPH_USER = 'carla'
    AGRAPH_PASSWORD = 'coroncina'

    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
            # 'tools.sessions.storage_type': 'file',
            # 'tools.sessions.storage_path': 'path',
            # 'tools.sessions.timeout': 60
        }
    }

    cherrypy.tree.mount(AllegroDB_Support_WebService(), '/', conf)
    cherrypy.config.update({
        "server.socket_host": "127.0.0.1",
        "server.socket_port": 8081})  # port
    cherrypy.engine.start()
    cherrypy.engine.block()


