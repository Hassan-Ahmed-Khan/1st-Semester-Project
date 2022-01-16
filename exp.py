def check():
    from operator import itemgetter
    import mysql.connector

    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='hassan543',
        port='3306',
        database='semproj'
    )
    cursor = mydb.cursor()
    import mysql.connector

    mydbb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='hassan543',
        port='3306',
        database='semproj'
    )
    cursor2 = mydbb.cursor()

    sql_command1 = "Select Email from adminsignup"
    sql_command2 = "Select Password from adminsignup"
    cursor.execute(sql_command1)
    cursor2.execute(sql_command2)
    #email = s1_entry.get()
    #password = s2_entry.get()
    e = []
    p = []
    for i in cursor:
        e.append(i)
    for j in cursor2:
        p.append(p)
    res = list(map(itemgetter(0), e))
    res2 = list(map(itemgetter(0), p))
    k = len(res)
    print(res)
    print(res2)


def data():
    cur = mydb.cursor()
    t = (s1_entry.get(), s2_entry.get())
    cur.execute('INSERT INTO admin_signup values(%s,%s)', t)
    s1_entry.delete(0, END)
    s2_entry.delete(0, END)

    mydb.commit()

check()