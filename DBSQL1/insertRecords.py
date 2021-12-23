import mysql.connector
try:
    dbobj = mysql.connector.connect(host='localhost', user="root", password="root", database="python-dec")
    dbcursor = dbobj.cursor()
    dbcursor.execute("insert into employees(eid, ename, esal)  values(101, 'Rahul Gandhi', 45000)")
    dbobj.commit()
    print("Data Inserted Successfully")

except mysql.connector.DatabaseError as e:
    dbobj.rollback()
    print("Rollback - Successfully", e)
finally:
    if dbcursor:
        dbcursor.close()
    if dbobj:
        dbobj.close()