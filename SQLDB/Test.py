import mysql.connector
dbobj = mysql.connector.connect(host="localhost", user="root", password="root", database="srini")
print(dbobj)
mydbcursor=dbobj.cursor()
print(mydbcursor)

mydbcursor.execute('select * from employee where ename="Gautham" ')
data= mydbcursor.fetchall()

print(data)
print(type(data))

for row in data:
    print(row)