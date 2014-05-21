#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import webapp2
import jinja2

from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader( os.path.dirname( __file__ ) ),
    extensions=[ "jinja2.ext.autoescape" ],
    autoescape=True )

class Salute(ndb.Model):
    name = ndb.StringProperty( required = True)
    time = ndb.DateTimeProperty( auto_now_add = True)

class SaluteHandler(webapp2.RequestHandler):
    def __init__(self, request= None, response= None):
        self.initialize( request, response )
        self.name = self.request.get( "name", "pobrecito hablador" )
        self.answer = ""

        try:
            self.name = self.request.get( "name" )
        except:
            self.answer = "<html><body><b>ERROR</b> " \
					"acquiring data</body></html>"

    def get(self):
        if (len(self.answer) == 0) :
            self.answer = self.name
        self.response.write(self.answer)

    def post(self):
        if (len(self.name) == 0) :
            self.name = "anonymous"

        if (len(self.answer) == 0) :
            self.name = self.name[ 0 ].upper() + self.name[1:]

            # Get all previous answers
            salutations = Salute.query().order( Salute.time );

            # Store the answer
            salute = Salute( name = self.name );
            salute.put();

            template_values = {
                'name': self.name,
                'salutations': salutations,
            }

            template = JINJA_ENVIRONMENT.get_template( "answer.html" )
            self.response.write( template.render( template_values ) );
        else:
            self.response.write(self.answer)


app = webapp2.WSGIApplication([
    ('/hi', SaluteHandler)
    ], debug=True)              
