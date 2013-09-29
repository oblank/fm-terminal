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
import urllib2



class MainHandler(webapp2.RequestHandler):
    def fetch(self, url):
        try:
            result = urllib2.urlopen(url)
            return result.read()
        except e:
            return "{\"error\":\"" + e.message + "\"}"
    def get_json_p(self):
        url = self.request.get('url');
        callback = self.request.get('callback');
        if callback:
            self.response.write(callback + "(")
        self.response.write(self.fetch(url))
        if callback:
            self.response.write(")");

    def get(self):
        self.get_json_p()
    def post(self):
        self.get_json_p()


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
