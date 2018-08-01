import datetime
import pymysql as mdb
import sys

from flask import Flask
from flask import g
from flask import render_template


app = Flask(__name__)


class Error(Exception):
  """The base error class."""


def log_to_console(message):
  """This is just a debug method."""
  fmt = '[%s]: %s' % (datetime.datetime.now(), message)
  print(fmt, file=sys.stderr)


def db_connect():
  """Connects to a MySQL DB and returns the connection.

  Returns:
    conn: A pymysql connection object.
  Raises:
    Error: mdb.Error. If there was a problem connecting to the DB.
  """
  user = 'root'
  passwd = 'strawberry'
  db = 'pets'
  #host = 'mysql.onedogtwodogs.com'
  try:
    conn = mdb.connect(user=user,
                       passwd=passwd,
                      # host=host,
                       db=db)
  except mdb.Error as e:
    raise Error(e)
  return conn


def get_db():
  """Opens a new db connection."""
  if not hasattr(g, 'db_conn'):
    g.db_conn = db_connect()
  return g.db_conn


@app.teardown_appcontext
def close_db(error):
  """Closes the db again at the end of the request."""
  if hasattr(g, 'db_conn'):
    # Connection must commit in order to execute.
    g.db_conn.commit()
    g.db_conn.close()


@app.route('/')
def hello_world():
  return 'Hello, World!'


if __name__ == '__main__':    
  app.run()
