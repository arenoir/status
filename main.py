"""`main` is the top level module for your Flask application."""

from flask import Flask
from flask import render_template

from google.appengine.api import urlfetch
from google.appengine.ext import db
#from google.appengine.api.app_identity import app_identity

from models.status_check import StatusCheck

app = Flask(__name__)

@app.route('/')
def hello():
  status_checks = db.GqlQuery("SELECT * FROM StatusCheck")
  return render_template('index.html', status="ok", status_checks=status_checks)


@app.route('/status_check')
def status_check():
  url = "https://fieldphone.com/"
  result = urlfetch.fetch(url)
  code = result.status_code
  status = 'ok'
  if result.status_code != 200:
    status = 'not_ok'

  check = StatusCheck(url=url, code=code, latency=300)
  check.put()
  return status

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
