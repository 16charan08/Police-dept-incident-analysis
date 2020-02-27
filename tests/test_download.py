
import os
import pytest
from project0 import p0

#url = 'http://normanpd.normanok.gov/filebrowser_download/657/2020-02-20%20Daily%20Incident%20Summary.pdf'
def test_fetchincidents():
    cwd = os.getcwd()
    print(cwd)
    try:
         assert open('./incidents.pdf', 'rb')
         print("Incidents files created")
    except:
        print("No file exsisted with that name; please try to execute main.py")


def test_extractincidents():

    try:
        a = p0.extractincidents()
        assert len(a)>1
        print("Data frame created")
    except:
        print("Error Data frame not created")


def test_dbcreated():
    try:
        database = '../project0/normanpd.db'
        print(database)
    except:
        print("Error Data frame not created")




test_fetchincidents()
test_extractincidents()
test_dbcreated()
