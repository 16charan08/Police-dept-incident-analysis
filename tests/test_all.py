import os
import sys
import pytest
import sqlite3
from sqlite3 import Error
from project0 import p0
import wget
#import p0

url = 'http://normanpd.normanok.gov/filebrowser_download/657/2020-02-26%20Daily%20Incident%20Summary.pdf'
database = 'normanpd.db'
def test_fetchincidents():
        assert open('./incidents.pdf', 'rb') is not None

def test_extractincidents():
    a = p0.extractincidents()
    assert len(a)>1

def test_dbcreated():
    dname = p0.createdb()
    assert dname == database

def test_data_inserted():
    dname = p0.createdb()
    a = p0.extractincidents()
    p0.populatedb(dname,a)
    sql = sqlite3.connect(database)
    cursor = sql.cursor()
    cursor.execute('''select * from incidents''')
    assert cursor.fetchall() is not None
    sql.close()


def test_status():
    dname = p0.createdb()
    a = p0.extractincidents()
    p0.populatedb(dname, a)
    p0.status(dname)
    sql = sqlite3.connect(database)
    cursor = sql.cursor()
    cursor.execute('''select nature,count(nature) from incidents group by nature order by nature''')
    assert cursor.fetchall() is not None
    sql.close()







