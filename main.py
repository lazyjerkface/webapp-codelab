# -*- coding: utf-8 -*-

import datetime
import pymysql as mdb
import sys

from flask import Flask
from flask import g
from flask import render_template


app = Flask(__name__)

# Constants
# Exercise 1a
HOSPITAL_NAME = 'Strawberry Hill'


# When a user visits the main page, this function returns and displays
# the content. Let's modify it!
# Exercise 1:
# a) At the top of the page, look for the declaration of HOSPITAL_NAME.
#    Let's update it to the name of your hospital.
#    When you're done, save the file, and refresh your hosptial's home page.
# b) The list of patients is... hard to visually digest. Instead of <p> tags,
#    use a <table> and wrap the rows in <tr> tags with each field wrapped
#    with <td> tags.  Don't forget the header row!
#    HINT:
#      <tr>
#        <td>1</td>
#        <td>Saint</td>
#        ...
#      </tr>
# c) Implement the render_template method below.
#    HINT: http://flask.pocoo.org/docs/1.0/quickstart/#rendering-templates
# d) (Optional): Look at static/css/styles.css, change some values,
#    and refresh the page.
@app.route('/')
def main_page():
  """This is the main page."""

  page_content = """
  <div><h1>%s</h1></div>
  <p><b>Patients:</b></p>
  """.strip() % HOSPITAL_NAME
  for patient_list in get_all_patients():
    # Exercise 1b
    page_content += '<p>%s</p>' % (', '.join(patient_list))
  return page_content
  # Exercise 1c
  #return render_template('main.html')


# Exercise 2:
#  a) Implement this method by redirecting users when clicking on a table row.
#     HINT: Look in static/js.
#  b) Create an HTML template and display it using the render_template method.
#  c) Display all the previous visits this patient has made.
#     HINT: see the get_patient_info method.
#  d) (Optional): Create a base template that all other templates can inherit.
#     HINT: http://flask.pocoo.org/docs/1.0/patterns/templateinheritance/
@app.route('/view/<account_num>')
def view_patient(account_num):
  """This page displays information about an individual patient."""

  page_content = ''
  visits_list = get_patient_info(account_num, table='visits')
  for visit in visits_list:
    page_content += '<p>' + ', '.join(visit) + '</p>'
  return page_content


# Exercise 3
#  a) Implement this method which adds a visit to the visit table
#     for a patient.
#  b) Think about the use-case and design.
#     Where does the user add in the visit info? How does the user get there?
#     Will data be submitted via form? AJAX call?
# There is a lot to consider, so take it one step at a time.
def add_visit(account_num):
  pass


# Exercise 4 (Optional)
# Implement methods allowing a user to edit existing data.
# For example, updating owner info in the pets table or
# updating the reason in the visits table.


class Error(Exception):
  """The base error class."""


def log_to_console(message):
  """This is just a debug method.

  Usage:
    log_to_console('view data or debug info in the console')
  """

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
  passwd = ''
  db = 'pets'
  try:
    conn = mdb.connect(user=user,
                       passwd=passwd,
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


def get_all_patients():
  """Returns a list of lists containing all patient info."""
  query = ('SELECT account_num, name, animal_type, gender, birthdate,'
           'owner_firstname, owner_lastname, owner_phone from pets')
  cur = get_db().cursor()
  cur.execute(query)
  patient_result_list = []
  for (account_num, name, animal_type, gender, birthdate, owner_firstname,
       owner_lastname, owner_phone) in cur.fetchall():
    # Converted non-string values to strings.
    patient_result_list.append([str(account_num), name, animal_type, gender,
                                birthdate.strftime('%Y-%m-%d'), owner_firstname,
                                owner_lastname, str(owner_phone)])
  return patient_result_list


def get_patient_info(account_num, table='pets'):
  query = 'SELECT * from %s WHERE account_num = %s' % (table, account_num,)
  cur = get_db().cursor()
  cur.execute(query)
  result = cur.fetchall()
  patient_info = []
  if not result:
    return patient_info
  for row in result:
    row_info = []
    for entry in row:
      formatted_entry = entry
      if isinstance(entry, int):
        formatted_entry = str(entry)
      elif isinstance(entry, datetime.date):
        formatted_entry = entry.strftime('%y-%m-%d')
      row_info.append(formatted_entry)
    # Strip the ID field
    patient_info.append(row_info[1:])
  return patient_info


if __name__ == '__main__':    
  app.run()
