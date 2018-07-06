#!/usr/bin/python
import pyodbc
user='sa'
password='PC#1234'
database='climate'
port='1433'
TDS_Version='8.0'
server='192.168.0.107'
driver='FreeTDS'

   con_string='UID=%s;PWD=%s;DATABASE=%s;PORT=%s;TDS=%s;SERVER=%s;driver=%s' % (user,password, database,port,TDS_Version,server,driver)
   cnxn=pyodbc.connect(con_string)
   cursor=cnxn.cursor()
   cursor.execute("INSERT INTO mytable(name,address) VALUES (%s,%s)" %('thavasi','mumbai'))
   cnxn.commit()
