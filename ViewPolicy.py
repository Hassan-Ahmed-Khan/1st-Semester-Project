def viewpolicy():
    # TKINTER LIBRARY
    from tkinter import Tk
    from tkinter import Canvas
    from tkinter import Button
    from tkinter import Entry
    from tkinter import Label
    from tkinter.font import Font
    sd = Tk()
    sd.title("View/Edit Policy")
    sd.geometry("1300x660")
    sd.configure(bg='#1F1D36')
    sd.resizable(0, 0)
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
    cur.execute('SELECT * FROM policy_edit')
    table = cur.fetchall()
    num1 = 180
    n = 1
    for i in table:
        l11 = Label(sd, text=n, font=norm3, bg='#1F1D36', fg='#EDEDED')
        l11.place(x=230, y=num1)
        n = n + 1
        policy_name = Label(sd, text=i[0], font=norm2, fg='#87AAAA', bg='#1F1D36')
        policy_name.place(x=250, y=num1)

        policy_Premium = Label(sd, text=i[1], font=norm2, fg='#87AAAA', bg='#1F1D36')
        policy_Premium.place(x=450, y=num1)

        policy_Premium = Label(sd, text=i[2], font=norm2, fg='#87AAAA', bg='#1F1D36')
        policy_Premium.place(x=650, y=num1)

        policy_Premium = Label(sd, text=i[3], font=norm2, fg='#87AAAA', bg='#1F1D36')
        policy_Premium.place(x=850, y=num1)

        policy_Premium = Label(sd, text=i[4], font=norm2, fg='#87AAAA', bg='#1F1D36')
        policy_Premium.place(x=1050, y=num1)

        num1 = num1 + 30

    # CANVAS STUFF
    can = Canvas(sd, width=203, height=1090, bg='#3F3351', )
    can.place(x=0, y=0)
    can2 = Canvas(sd, width=1200, height=100, bg='#3F3351')
    can2.place(x=205, y=0)

    # LABLE FRONT PAGE
    text1 = Label(sd, text="IMS", font=norm1, bg='#3F3351', fg='#EDEDED')
    text1.place(x=220, y=20)
    text = Label(sd, text="Insurance Management System.", font=norm, bg='#3F3351', fg='#EDEDED')
    text.place(x=220, y=50)
    text1 = Label(sd, text="Policy View/Edit.", font=norm1, bg='#3F3351', fg='#EDEDED')
    text1.place(x=790, y=30)

    # exit button
    exit_btn = Button(sd, text="Exit", width=13, bg='#EDEDED', command=sd.quit)
    exit_btn.place(x=50, y=590)

    # DASHBOARD BUTTON
    def comb1():
        sd.destroy()
        adminfront()

    dashboard_button = Button(sd, text="Dashboard", width=10, bg='#3F3351', fg='#EDEDED', font=norm1, borderwidth=0,
                              command=comb1)
    dashboard_button.place(x=4, y=250)

    def onbutton(e):
        dashboard_button['bg'] = '#1F1D36'

    def leavebutton(e):
        dashboard_button['bg'] = '#3F3351'
        dashboard_button.bind('<Enter>', onbutton)
        dashboard_button.bind('<Leave>', leavebutton)

    dashboard_button.bind('<Enter>', onbutton)
    dashboard_button.bind('<Leave>', leavebutton)

    # REFRESH BUTTON
    refresh_button = Button(sd, text="Refresh", width=10, bg='#3F3351', fg='#EDEDED', font=norm1, borderwidth=0)
    refresh_button.place(x=4, y=350)

    def onbutton(e):
        refresh_button['bg'] = '#1F1D36'

    def leavebutton(e):
        refresh_button['bg'] = '#3F3351'
        refresh_button.bind('<Enter>', onbutton)
        refresh_button.bind('<Leave>', leavebutton)

    refresh_button.bind('<Enter>', onbutton)
    refresh_button.bind('<Leave>', leavebutton)

    # ENTRIES LABLES FOR ADD POLICY
    tpp_label = Label(sd, text="Policy Name", fg='#EDEDED', bg='#1F1D36', font=norm2)
    tpp_label.place(x=250, y=150)

    pnn_label = Label(sd, text="Policy Premimum", fg='#EDEDED', bg='#1F1D36', font=norm2)
    pnn_label.place(x=450, y=150)

    ptt_label = Label(sd, text="Policy Tenure", fg='#EDEDED', bg='#1F1D36', font=norm2)
    ptt_label.place(x=650, y=150)

    ppp_label = Label(sd, text="Sum Assurance", fg='#EDEDED', bg='#1F1D36', font=norm2)
    ppp_label.place(x=850, y=150)

    saa_label = Label(sd, text="Policy Type", fg='#EDEDED', bg='#1F1D36', font=norm2)
    saa_label.place(x=1050, y=150)

    # EDIT BUTTON
    # edit_btn = Button(sd, text="Edit", width=7, fg='#1F1D36', bg='#EDEDED')
    # edit_btn.place(x=1200, y=250)

    # edit_btn = Button(sd, text="Edit", width=7, fg='#1F1D36', bg='#EDEDED')
    # edit_btn.place(x=1200, y=350)

    # edit_btn = Button(sd, text="Edit", width=7, fg='#1F1D36', bg='#EDEDED')
    # edit_btn.place(x=1200, y=450)

    # edit_btn = Button(sd, text="Edit", width=7, fg='#1F1D36', bg='#EDEDED')
    # edit_btn.place(x=1200, y=550)

    sd.mainloop()