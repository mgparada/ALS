import os
import sys
import jinja2
import webapp2
import hashlib
import time

from google.appengine.ext import ndb
from webapp2_extras import sessions

JINJA_ENVIRONMENT = jinja2.Environment(
 loader=jinja2.FileSystemLoader( os.path.dirname( __file__ ) ),
 extensions=[ "jinja2.ext.autoescape" ],
 autoescape=True )

# credit:  Nick Johnson of Google
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

class User(ndb.Model):
    name = ndb.StringProperty( required = True )
    email = ndb.StringProperty( required = True )
    password = ndb.StringProperty( required = True )
    

class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)
 
        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)
 
    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()
    
class UserHandler(BaseHandler):
    def __init__ (self, request=None, response=None):
        self.initialize(request, response)
        self.name = self.request.get( "name" )
        self.email = self.request.get( "email" )
        self.password = self.request.get( "password" )
        
    def checkEmail(self):
        if User.query( User.email == self.email ).fetch() == []: 
            to_response = True 
        else:
            to_response = False
            
        self.response.write( to_response )
        
    def doLogin(self):
        user = User.query( User.email == self.email ).fetch()
        h = hashlib.md5()
        h.update(self.password)        
        
        if user == []:
            self.response.write( False )
            return False
        
        if user[0].email == self.email and user[0].password == h.hexdigest():
            self.response.set_cookie('login', "1")
            self.response.set_cookie("email", self.email)
            self.response.write( True )
        else:
            self.response.write( False )
            
    def doLogout(self):
        self.response.delete_cookie("login")
        self.response.delete_cookie("email")
        self.redirect("/")
        
    def post(self):
        h = hashlib.md5()
        h.update(self.password)
        
        user = User(name = self.name, email = self.email, password = h.hexdigest())
        user.put()
        
        time.sleep(0.2)
        self.response.set_cookie("login", "1")
        self.response.set_cookie("email", self.email)
        self.redirect("/dash")
        
    def change(self):
        print self.request.get("element")

class DashboardHandler(UserHandler):
    def __init__(self, request=None, response=None):
        self.initialize(request, response)
        
    def get(self):
        print self.request.cookies.get("login")
        if self.request.cookies.get("login") == None:
            self.redirect("/")
        else:
            user = User.query( User.email == self.request.cookies.get("email") ).fetch()
            template_values = {
                'name': user[0].name,
                'email': user[0].email
            }
                
            template = JINJA_ENVIRONMENT.get_template( "dashboard.html" )
            self.response.write( template.render(template_values) )
        
    def factura(self):
        if self.request.cookies.get("login") == None:
            self.redirect("/")
        else:
            user = User.query( User.email == self.request.cookies.get("email") ).fetch()
            template_values = {
                'name': user[0].name
            }
                
            template = JINJA_ENVIRONMENT.get_template( "dashboard_factura.html" )
            self.response.write( template.render(template_values) )
            
config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'claveSecreta',
}        

app = webapp2.WSGIApplication([
   webapp2.Route('/register/checkEmail', handler="main.UserHandler", handler_method="checkEmail"),
   webapp2.Route('/register/doLogin', handler="main.UserHandler", handler_method="doLogin"),
   webapp2.Route('/register/doLogout', handler="main.UserHandler", handler_method="doLogout"),
   webapp2.Route('/register/changeProperty', handler="main.UserHandler", handler_method="change"),
   webapp2.Route('/dash/factura', handler="main.DashboardHandler", handler_method="factura"),
   ('/register', UserHandler),
   ('/dash', DashboardHandler),
   ], debug=True, config=config)
