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
 - **fetchincidents(url)** \
This function takes one arugument url which is passed in main function. This url is used to download data using *wget.download(url)* to our local directory with name *incidents.pdf*. If file is already exsisted it will remove it and always create only one *incidents.pdf*, it is later on used in further investigation of our incidents. \

- **extractincidents()** \
 This function takes no arguments but reads *incidents.pdf* that stored in using fetchincidents(url), extracts raw data from pdf and stores in a list for further use.We can split this extraction mainly into 3 steps
<br/> \
**step1:-** \
 With*PyPDF2* data is extracted from *incidents.pdf* with following commands\
 > *pdfFileObj = open('./incidents.pdf', 'rb') \
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)* 
    
 The PdfFileReader function of the PyPDF2 package retrieves the data. The data obtained is not formatted and contains excess data which is   not required.   
 <br/> \
**step2:-**  \
**_Assumptions made in this step are:-_** *Incident ORI* column having only 3 values that are used to detect end of each line(*OK0140200,14005,EMSSTAT*). \
After data is extracted using *PdfFileReader()* then each page is read and converted to text using *getPage(n) and extractText()* respectively.\
> *pageObj = pdfReader.getPage(n).extractText()* 

Every ';' ,'Tilde-','Tilde' are replaced by space(' ') in order to handle latitude and longitude locations. \
> *pageObj = re.sub(';',' ',pageObj) \
        pageObj = re.sub('Tilde-',' ',pageObj) \
        pageObj = re.sub('Tilde', ' ', pageObj)*

The data in a single row can be present in multiple lines, so the excess '\n' must be replaced with a space so as to regard them a single column after parsing. Carefully observing the pattern ' \n' (single space followed by a new line) is replaced with a single space using *replace()*. Now according to our assumption from text data we will get last column as (Incident ORI\n, OK0140200\n , 14005\n ,EMSSTAT\n) which will be replaced by ((Incident ORI;) ,(OK0140200;) , (14005;) ,(EMSSTAT;)). This implies that to find and split at end of each line '\n' is replaced with ';' as below.
>*pageObj = 
        pageObj = pageObj.replace('OK0140200\n','OK0140200;').replace('Incident ORI\n','Incident ORI;').\
                  replace('14005\n','14005;').replace('EMSSTAT\n','EMSSTAT;').replace(' \n',' ')*

<br/> \
**step3:-**  \   
**_Assumptions made in this step are:-_** Missing values will only be noted in *Nature column* , Because in most of the cases Incident loaction , Incident number (given by police), date/time , Incident ORI will be known as they are determined values. But Nature of the incident may not be known because of lack of evidences or withness etc. So, I am assuming only that value misses. \

Text is spilt at ';' and then each row is stored into a list. This list length is checked if it is lessthan 5 then "Null" is inserted at position of list according to our assumptions. 

> *text = pageObj.split(";") \
        text = text[:-1] \
        for j in range(0,len(text)): \
            text[j] = text[j].split("\n") \
            if len(text[j]) == 4: \
                text[j].insert(3,"Null") \
            df.append(tuple(text[j]))*
            
At last it is appended to list of tuples to maintain order(as tuple preserves order). This this list is retruned for further usages.

- **createdb()** \
A database is created using the function dbCreate. The database is named normanpd.db and contains one table names incidents.The sqlite3 package opens the connection creating a normanpd.db database file and the cursor and execute functions are used to execute the queries within the database from python. Initially the database is checked for any table named incidents and if found the table is dropped. 

>*cursor.execute('''DROP TABLE IF EXISTS incidents''') \
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS incidents(incident_time TEXT,
            incident_number TEXT,
            incident_location TEXT,
            nature TEXT,
            incident_ori TEXT)
            ''')*
            
- **populatedb(db, incidents)** \
The dbInsert function takes two arguments which are the database name from dbCreate function and the incidents data from dataExtract function. This function opens a connection to the database 'normanpd.db' and inserts the rows from the incidents data into the database.

>*cursor.execute('''INSERT INTO incidents(incident_time,
    incident_number,
    incident_location,
    nature,
    incident_ori)
                          VALUES(?,?,?,?,?)''', incidents[i])*
  

- **status(db)** \
 This function takes one argument which is database name from dbCreate to get nature and number of times each nature occured in each pdf respectively.
 
 >*cursor.execute('''select nature,count(nature) from incidents group by nature order by nature''')*
 
 ### setup.py and setup.cfg
The setup.py file is required for finding the packages within the project during the execution. It finds the packages automatically.The setup.cfg file is required for running the pytest command to perform tests on the program.

### test_all.py

