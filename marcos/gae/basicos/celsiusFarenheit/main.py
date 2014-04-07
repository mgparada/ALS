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

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

class MainHandler(webapp2.RequestHandler):
	def __init__(self, request=None, response=None):
		self.initialize(request, response)
		self.gradesFar = 0
		self.gradesCel = 0
		self.answer = ""

		try:
			self.gradesFar = float(self.request.get( "gradesFar" ))
		except:
			self.answer = "<html><body><b>ERROR</b> " \
					"acquiring data</body></html>"

	def get(self):
		self.response.write('Hello world!')

	def post(self):
		#if (is_number(self.gradesFar):
		#if (isinstance(self.gradesFar, (int, long, float, complex)):
		if (self.gradesFar != 0):
			self.gradesCel = (self.gradesFar - 32) / 1.8;
			self.answer = str.format("<html><body>Resultado (celsius): {0}<form input type='button' onClick='history.go(-1); return true;'></html>", self.gradesCel)
		else:
			self.answer = "<html><body>ERROR de SINTAXIS: Debe introducir un numero distinto de 0.</body></html>"
			
		self.response.write(self.answer)

app = webapp2.WSGIApplication([
	('/convert', MainHandler)
	], debug=True)
