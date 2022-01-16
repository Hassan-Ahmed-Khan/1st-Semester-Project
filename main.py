import mysql.connector
mydb= mysql.connector.connect(
    host='localhost',
    user='root',
    password='hassan543',
    port='3306',
    database ='semproj'
    )
cur= mydb.cursor()
cur.execute('CREATE TABLE policy_edit(Name varchar(20),Premium int,Tenure int,Deductable int) ')
