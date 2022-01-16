def registeredusers():
    # TKINTER LIBRARY
    from tkinter import Tk
    from tkinter import END
    from tkinter import Canvas
    from tkinter import Button
    from tkinter import Entry
    from tkinter import Label
    from tkinter.font import Font
    # import Adminfp
    sv = Tk()
    sv.title("Registered Users")
    sv.geometry("1250x660")
    sv.configure(bg='#1F1D36')
    sv.resizable(0, 0)
    norm = Font(family="Verdana", size=15, weight="bold", slant="italic")
    norm1 = Font(family="Verdana", size=20, weight="bold", slant="italic")
    norm2 = Font(family="Verdana", size=10, weight="bold", slant="italic")
    norm3 = Font(family="Verdana", size=7, weight="bold", slant="italic")

    # SQL CONNECTION
    import mysql.connector
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='hassan543',
        port='3306',
        database='semproj'
    )

    cur = mydb.cursor()
    cur.execute('SELECT * FROM signup')
    table = cur.fetchall()


    num1 = 180
    n = 1
    for i in table:
        l11 = Label(sv, text=n, font=norm3, bg='#1F1D36', fg='#EDEDED')
        l11.place(x=230, y=num1)
        n = n + 1
        full_name = Label(sv, text=i[0], font=norm2, fg='#87AAAA', bg='#1F1D36')
        full_name.place(x=250, y=num1)

        Address_label = Label(sv, text=i[1], font=norm2, fg='#87AAAA', bg='#1F1D36')
        Address_label.place(x=450, y=num1)

        mobile_no = Label(sv, text=i[3], font=norm2, fg='#87AAAA', bg='#1F1D36')
        mobile_no.place(x=800, y=num1)

        email = Label(sv, text=i[4], font=norm2, fg='#87AAAA', bg='#1F1D36')
        email.place(x=1000, y=num1)


        num1 = num1 + 30

    # CANVAS STUFF
    can = Canvas(sv, width=203, height=1090, bg='#3F3351', )
    can.place(x=0, y=0)
    can2 = Canvas(sv, width=1200, height=100, bg='#3F3351')
    can2.place(x=205, y=0)

    # LABLE FRONT PAGE
    text1 = Label(sv, text="IMS", font=norm1, bg='#3F3351', fg='#EDEDED')
    text1.place(x=220, y=20)
    text = Label(sv, text="Insurance Management System.", font=norm, bg='#3F3351', fg='#EDEDED')
    text.place(x=220, y=50)
    text1 = Label(sv, text="Registered Users.", font=norm1, bg='#3F3351', fg='#EDEDED')
    text1.place(x=890, y=30)

    # exit button
    exit_btn = Button(sv, text="Exit", width=13, bg='#EDEDED', command=sv.quit)
    exit_btn.place(x=50, y=590)

    # DASHBOARD BUTTON
    def comb1():
        sv.destroy()
        #adminfront()

    dashboard_button = Button(sv, text="Dashboard", width=10, bg='#3F3351', fg='#EDEDED', font=norm1, borderwidth=0,
                              command=comb1)
    dashboard_button.place(x=4, y=250)

    def onbutton(e):
        dashboard_button['bg'] = '#1F1D36'

    def leavebutton(e):
        dashboard_button['bg'] = '#3F3351'

    dashboard_button.bind('<Enter>', onbutton)
    dashboard_button.bind('<Leave>', leavebutton)

    # ENTRIES LABLES FOR ADD POLICY
    fnn_label = Label(sv, text="Full Name", fg='#EDEDED', bg='#1F1D36', font=norm2)
    fnn_label.place(x=250, y=150)

    add_label = Label(sv, text="Address", fg='#EDEDED', bg='#1F1D36', font=norm2)
    add_label.place(x=450, y=150)

    mbb_label = Label(sv, text="Mobile no.", fg='#EDEDED', bg='#1F1D36', font=norm2)
    mbb_label.place(x=800, y=150)

    emm_label = Label(sv, text="Email", fg='#EDEDED', bg='#1F1D36', font=norm2)
    emm_label.place(x=1000, y=150)

    sv.mainloop()


registeredusers()