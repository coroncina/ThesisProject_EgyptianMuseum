import random
import string
import cherrypy
import json
import pymongo


###preparazione x USER PROFILE MANAGER
# 1) ricevere i dati dal client tramite rest
# 2) interpretarli e salvarli in db

"""LINK UTILI
https://www.tutorialspoint.com/cherrypy/
https://docs.cherrypy.org/en/latest/tutorials.html
https://riptutorial.com/cherrypy
https://github.com/cherrypy/cherrypy/tree/master/cherrypy/tutorial
https://github.com/GrafeasGroup/tor_core/tree/master/tor_core
"""

#dumps fa diventare json

def prendiParametri(vis_id, op_id):
    print("-------")
    print(vis_id, op_id)

@cherrypy.expose
class StringGeneratorWebService(object):

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return cherrypy.session['mystring']

    def POST(self):
        cl = cherrypy.request.headers['Content-Length']
        jData = cherrypy.request.body.read(int(cl))
        rawData = json.loads(jData)
        print(jData)
        id_visitatore = rawData['visitatore']['id_visitatore']
        id_opera = rawData['visitatore']['opere'][0]['opera']['id_opera']
        #prendiParametri(id_visitatore, id_opera)
        #print(id_visitatore)
        #print(id_opera)

        return "ok"

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
    cherrypy.tree.mount(StringGeneratorWebService(), '/', conf)
    cherrypy.config.update("server_UPM.conf")       #port
    cherrypy.engine.start()
    cherrypy.engine.block()

    id_op = StringGeneratorWebService()
    print(id_op.POST())

    # def start_heartbeat_server():
    #     """
    #     Starts the cherrypy heartbeat server. Do not call directly; use
    #     configure_heartbeat() instead.
    #     :return: None
    #     """
    #     cherrypy.tree.mount(heartbeat(), '/', conf)
    #     cherrypy.server.socket_host = "127.0.0.1"
    #     cherrypy.engine.start()
    #     logging.info('Cherrypy heartbeat started!')
    #
    #
    # def stop_heartbeat_server():
    #     """
    #     Stops the cherrypy heartbeat server. I guess you can call this one
    #     directly if you need to, but I recommend using
    #     tor_core.helpers.stop_heartbeat() instead, since any other items relevant
    #     to shutting down the heartbeat will go there.
    #     :return: None
    #     """
    #     cherrypy.engine.exit()