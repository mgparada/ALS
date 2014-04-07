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
# import webapp2

# class MainHandler(webapp2.RequestHandler):
#     def get(self):
#         self.response.write('Hello world!')

# app = webapp2.WSGIApplication([
#     ('/', MainHandler)
# ], debug=True)

import webapp2

class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write("<!DOCTYPE HTML>"
			"<html><head></head>"
			"<body><form id='ecoForm' action='/' method='post'>"
			"<input type='text' id='content' name='content'></input>"
			"<input type='submit' value='Enviar'></input>"
			"</form></body></html>"
		)

	def post(self):
		content = self.request.get('content')
		print content
		self.response.write(content)


app = webapp2.WSGIApplication([
	('/', MainHandler)
	], debug=True)