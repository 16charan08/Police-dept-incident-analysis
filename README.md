# cs5293p19-project0
In this project a PDF file is downloaded from the Norman Police Deparatment and the data regarding the incidents is inserted into a SQLite database named 'normanpd.db'. The downloaded PDF file contains the incidents reports in the Norman area. The PDF file is cleaned using python and the data is formatted into the form of rows. A random row can be retrieved from the database after inserting the rows into the database.

### Structure
Screenshot of tree here

### Packages installed/used 
pipenv install PyPDF2 &nbsp; \
pipenv install pandas &nbsp; \
pipenv install wget &nbsp;\
import sqlite3 \
import re \
import pytest \
 

#### project0--main.py
main.py contains all function calls for each functionality \
###### p0.fetchincidents(url) \
###### incidents = p0.extractincidents() \
###### db = p0.createdb() \
###### p0.populatedb(db, incidents) \
###### p0.status(db) \
