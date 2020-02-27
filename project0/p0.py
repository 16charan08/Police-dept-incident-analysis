import os
import io
import sqlite3
from sqlite3 import Error
import PyPDF2
import pandas as pd
import wget
import re

def fetchincidents(url):
    cwd = os.getcwd()  # Get the current working directory (cwd)
    print(cwd)

    file = os.listdir(cwd)
    #print(file)
    if os.path.exists("./docs/incidents.pdf"):
        os.remove("./docs/incidents.pdf")
        wget.download(url,'./docs/incidents.pdf')
    else:
        wget.download(url,'./docs/incidents.pdf')
    #wget.download(url, '/incidents.pdf')
def extractincidents():
    cwd = os.getcwd()  # Get the current working directory (cwd)
    pdfFileObj = open('./docs/incidents.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
   # print()
    df = []
    for i in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(i).extractText()
        pageObj = re.sub(';',' ',pageObj)
        pageObj = pageObj.replace('OK0140200\n','OK0140200;').replace('Incident ORI\n','Incident ORI;').\
                  replace('14005\n','14005;').replace('EMSSTAT\n','EMSSTAT;').replace(' \n',' ')
        text = pageObj.split(";")
        text = text[:-1]
       # print(text)
        for j in range(0,len(text)):
            text[j] = text[j].split("\n")
            if len(text[j]) == 4:
                text[j].insert(3,"Null")
            df.append(tuple(text[j]))
    print(len(df))
   # print(df)
    return df

def createdb():
    try:
        sqlite3.connect(':memory:')
        db = sqlite3.connect('normanpd.db')
        cursor = db.cursor()
        cursor.execute('''DROP TABLE IF EXISTS incidents''')
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS incidents(incident_time TEXT,
            incident_number TEXT,
            incident_location TEXT,
            nature TEXT,
            incident_ori TEXT)
            ''')
        db.commit()
    except Error as e:
        print(e)
    return db

def populatedb(db, incidents):
    cursor = db.cursor()
    #print(incidents[2][0])
    for i in range(1,len(incidents)):
        cursor.execute('''INSERT INTO incidents(incident_time,
    incident_number,
    incident_location,
    nature,
    incident_ori)
                          VALUES(?,?,?,?,?)''', incidents[i])
    db.commit()
    cursor.execute('''select * from incidents''')
   # print(cursor.fetchall())


def status(db):
    cursor = db.cursor()
    cursor.execute('''select nature,count(nature) from incidents group by nature''')
    print(cursor.fetchall())
    return



