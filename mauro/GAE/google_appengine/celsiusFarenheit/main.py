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
import lib
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader( os.path.dirname( __file__ ) ),
extensions=[ "jinja2.ext.autoescape" ],
autoescape=True )

class MainHandler(webapp2.RequestHandler):
    def __init__(self, request = None, response = None):
	self.initialize(request, response)
	self.number = 0
	self.option = "celsius"
	self.answer = ""
	self.result = 0

	try:
		self.number = self.request.get("number")
		self.option = self.request.get("option")
	except:
		self.answer = "<html><body><b>ERROR</b> " \
                                        "acquiring data</body></html>"

    def get(self):
        self.response.write('Hello world!')
	
    def post(self):
	if self.option == "celsius":
		self.result = lib.gradosCelsiusFarenheit(int(self.number))
		template_values = {
			'celsius': self.number,
			'farenheit': self.result
		}
		template = JINJA_ENVIRONMENT.get_template( "celsius.html" )
	else:
		self.result = lib.gradosFarenheitCelsius(int(self.number))
		template_values = {
			'farenheit': self.number,
			'celsius': self.result
		}
		template = JINJA_ENVIRONMENT.get_template( "farenheit.html" )
	
	self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/convert', MainHandler)
], debug=True)
