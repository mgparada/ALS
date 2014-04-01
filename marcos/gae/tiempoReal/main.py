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
import time

class MainHandler(webapp2.RequestHandler):
	def __init__(self, request = None, response = None):
		self.initialize(request, response)
		self.answer = ""

	def get(self):
		actualHour = time.asctime( time.localtime(time.time()) )
		spaces = 0
		i = 0

		while (spaces < 3):
			if (actualHour[i] == " "):
				spaces += 1
				if (spaces == 3):
					now = actualHour[i+1:]
					pos = now.find(" ")
					now = now[0:pos]
			i += 1

		self.answer = "<html><body>La hora actual es " + now + "</body></html>"
		self.response.write(self.answer)
		
app = webapp2.WSGIApplication([
	('/', MainHandler)
	], debug=True)