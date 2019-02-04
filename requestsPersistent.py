"""
import requests

s = requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")

print(r.text)
"""

"""
from requests import Request, Session

s = Session()
url = 'http://127.0.0.1:8080/'
data ='ciao sono lucia e sono una sirena'
headers = {'carla':'user'}
req = Request('GET',  url,
    data=data,
    headers=headers)

prepped = s.prepare_request(req)

# fate qualcosa con prepped.body
# fate qualcosa con prepped.headers

resp = s.send(prepped)

print(resp.status_code)

"""



import time

import cherrypy

class TimingTool(cherrypy.Tool):
    def __init__(self):
        cherrypy.Tool.__init__(self, 'before_handler',
                               self.start_timer,
                               priority=95)

    def _setup(self):
        cherrypy.Tool._setup(self)
        cherrypy.request.hooks.attach('before_finalize',
                                      self.end_timer,
                                      priority=5)

    def start_timer(self):
        cherrypy.request._time = time.time()

    def end_timer(self):
        duration = time.time() - cherrypy.request._time
        cherrypy.log("Page handler took %.4f" % duration)

cherrypy.tools.timeit = TimingTool()

class Root(object):
    @cherrypy.expose
    @cherrypy.tools.timeit()
    def index(self):
        return "hello world"


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        }
    }

cherrypy.quickstart(Root(), '/', conf)



