import mysql.connector
dbobj = mysql.connector.connect(host="localhost", user="root", password="root", database="6am")

if dbobj != None:
    print('Connection Successfull')
else:
    print('Connection Failed')

dbobj.close()