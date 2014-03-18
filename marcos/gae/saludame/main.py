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
import webapp2

class MainHandler(webapp2.RequestHandler):
    def __init__(self, request=None, response=None):
        self.initialize( request, response )
        self.name = ""
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
            self.name = self.name[ 0 ].upper() + self.name[ 1: ]
            self.answer = str.format( "<html><body>"
		    				"<b>Hola, {0}</b><form>""<INPUT Type='button'"
							"VALUE='<<' onClick="
							"'history.go(-1);"
							"return true;'>"
							"</form></body></html>",
			  				self.name )
        self.response.write(self.answer)

app = webapp2.WSGIApplication([
    ('/hi', MainHandler)
], debug=True)
