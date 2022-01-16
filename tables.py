import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='hassan543',
    port='3306',
    database = 'semproj'
    )

cu = mydb.cursor()
cu.execute('create table policy_holders(Full_name varchar(50), Email varchar(50) )')



