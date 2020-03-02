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
import pytest 
 

### project0--main.py
main.py contains all function calls for each functionality \
 **p0.fetchincidents(url) ,incidents = p0.extractincidents() ,db = p0.createdb() ,p0.populatedb(db, incidents) ,p0.status(db)**

After cloning repository, main.py is executed by following command in SSH 
> pipenv run python project0/main.py --incidents url \
By giving url of certain incident file here it will fetch all incidents and will store in 'normanpd.db' database

### project0--p0.py
The p0.py file contains the methods to download PDF, extract data, create a database, insert data into database and retrieve nature of incidents by its occurance.\
- **p0.fetchincidents(url)** \
This function takes arugument url which is passed in main function. This url is used to download data using *wget.download(url)* to our local directory with name *incidents.pdf*. If file is already exsisted it will remove it and always create only one *incidents.pdf*, it is later on used in further investigation of our incidents. \

- **p0.extractincidents()** \
 This function extracts raw data from pdf and stores in a dataframe for further use.We can split this extraction mainly into 3 steps
<br/> \
**step1:-** \
 With*PyPDF2* data is extracted from *incidents.pdf* with following commands\
 *pdfFileObj = open('./incidents.pdf', 'rb') \
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)* \
 The PdfFileReader function of the PyPDF2 package retrieves the data. The data obtained is not formatted and contains excess data which is   not required.   
 <br/> \
**step2:-** 


