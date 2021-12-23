import mysql.connector
try:
    dbobj = mysql.connector.connect(host='localhost', user="root", password="root", database="python-dec")
    # if dbobj:
    #     print("Connection Successfull!")
    dbcursor = dbobj.cursor()
    dbcursor.execute('create table employees(eid int, ename varchar(20), esal double(10,2))')
    print("Table Created Successfully")



except mysql.connector.DatabaseError as e:
    print("except block executing!",e)

finally:
    print("Finally Block always exectuted")
    if dbobj:
        dbobj.close()