import datetime
from google.appengine.ext import db
from google.appengine.api import users

class StatusCheck(db.Model):
  url = db.StringProperty(required=True, indexed=True)
  code = db.IntegerProperty(required=True)
  latency = db.IntegerProperty()
  created = db.DateTimeProperty(auto_now_add=True, indexed=True)
