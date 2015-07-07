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

# Make sure to run app like so:
# dev_appserver.py --datastore_consistency_policy=consistent [path_to_app_name]
# in order to see changes reflected in the redirect immediately

# To clear the datastore:
# /usr/local/google_appengine/dev_appserver.py --clear_datastore=1 [path_to_app_name]

import os
import webapp2
import jinja2
from google.appengine.ext import ndb


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# Define a Student model for the Datastore
class Student(ndb.Model):
    name = ndb.StringProperty(required=True)
    university = ndb.StringProperty(required=True)
    age = ndb.IntegerProperty(required=False)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        # Get all of the student data from the datastore
        student_query = Student.query()
        student_data = student_query.fetch()
        # Pass the data to the template
        template_values = {
            'students' : student_data
        }
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

    def post(self):
        # Get the student name and university from the form
        name = self.request.get('name')
        univ = self.request.get('univ')
        # Create a new Student and put it in the datastore
        student = Student(name=name, university=univ)
        student.put()
        # Redirect to the main handler that will render the template
        self.redirect('/')



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
