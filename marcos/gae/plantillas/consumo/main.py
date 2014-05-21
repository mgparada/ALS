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
	def __init__(self, request=None, response=None):
		self.initialize( request, response )
		self.answer = ""
		self.km = 0
		self.avgCons = 0
		self.hours = 0
		self.minutes = 0
		self.seconds = 0

		try:
			self.km = float(self.request.get( "km" ))
			self.avgCons = float(self.request.get( "avgCons" ))
			self.hours = float(self.request.get( "hours" ))
			self.minutes = float(self.request.get( "minutes" ))
			self.seconds = float(self.request.get( "seconds" ))
		except:
			self.answer = "<html><body><b>ERROR</b> " \
			"acquiring data</body></html>"

	def get(self):
		self.response.write('Hello world!')

	def post(self):
		timeInSeconds = self.hours * 60 * 60 + self.minutes * 60 + self.seconds
		if (self.km > 0 and self.avgCons > 0 and timeInSeconds > 0):
			totalConsumption = self.km * self.avgCons * timeInSeconds
			avgVelocity = self.km / (timeInSeconds / 60 / 60)

			template_values = {
				'totalConsumption' : totalConsumption,
				'avgVelocity' : avgVelocity
			}

			template = JINJA_ENVIRONMENT.get_template('answer.html');
			self.answer = template.render(template_values);
		else:
			self.answer = "<html><body>ERROR: Introducir numeros mayores que 0.</body></html>"

		self.response.write(self.answer)

app = webapp2.WSGIApplication([
	('/calc', MainHandler)
	], debug=True)
