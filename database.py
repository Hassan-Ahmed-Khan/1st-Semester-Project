import mysql.connector
mydb= mysql.connector.connect(
    host='localhost',
    user='root',
    password='hassan543',
    port='3306',
    database ='semproj'
    )
cur= mydb.cursor()
cur.execute('INSERT INTO policy_edit values("House",7400,51,4040)')
mydb.commit()