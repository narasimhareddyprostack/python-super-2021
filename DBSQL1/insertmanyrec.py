import mysql.connector
try:
    dbobj = mysql.connector.connect(host='localhost', user="root", password="root", database="python-dec")
    dbcursor = dbobj.cursor()
    sql = 'insert into emp(eid, ename, esal) values(%s,%s,%s)'
    data=[(103,'Rahul Gandhi -x', 45000),(104, "Sonia Gandhi-x ", 65000)]
    dbcursor.executemany(sql,data)
    dbobj.commit()
    print("Inserted Data Successfuylly")

except mysql.connector.DatabaseError as e:
    dbobj.rollback()
    print("Rollback - Successfully", e)
finally:
    if dbcursor:
        dbcursor.close()
    if dbobj:
        dbobj.close()