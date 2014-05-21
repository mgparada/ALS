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
import os
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
		loader=jinja2.FileSystemLoader( os.path.dirname( __file__ ) ),
		extensions=[ "jinja2.ext.autoescape" ],
		autoescape=True )

class MainHandler(webapp2.RequestHandler):
	def __init__(self, request, response):
		self.initialize(request, response)
		self.values = {
			'cif': self.request.get('cif'),
			'nombre': self.request.get('nombre'),
			'direccion': self.request.get('direccion'),
			'cp': self.request.get('cp'),
			'pais': self.request.get('pais'),
			'contacto': self.request.get('contacto'),
			'email': self.request.get('email'),
			'telefono': self.request.get('telefono')
			}


	def get(self):
		self.response.write('Hello world!')

	def post(self):
		factTemplate = JINJA_ENVIRONMENT.get_template('facturas.html')
		self.response.write( factTemplate.render(self.values) )

app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/facturas', MainHandler)
	], debug=True)
