import webapp2
from google.appengine.api import urlfetch
import logging
import urllib

class AddHandler(webapp2.RequestHandler):
  def post(self):
    logging.info("in request")
    url = "https://www.instapaper.com/api/add"
    body = {
      "username": self.request.get("username"),
      "password": self.request.get("password"),
      "url": self.request.get("url")
    }
    fetchdata = urlfetch.fetch(url, method = "POST", payload = urllib.urlencode(body))
    self.response.headers['Content-type'] = fetchdata.headers['Content-type']
    self.response.headers['Content-Location'] = fetchdata.headers['Content-Location']
    self.response.headers['X-Instapaper-Title'] = fetchdata.headers['X-Instapaper-Title']
    self.response.set_status(fetchdata.status_code)
    self.response.out.write(fetchdata.content)
