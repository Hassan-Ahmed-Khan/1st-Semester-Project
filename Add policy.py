def pe():
 from tkinter import END
 from tkinter.font import Font
 from tkinter import Tk
 from tkinter import Canvas
 from tkinter import Button
 from tkinter import Entry
 from tkinter import Label
 from Adminfp import adminfront
 hex = Tk()
 hex.title("IMS")
 hex.geometry("1090x660")
 hex.resizable(0,0)
 hex.configure(bg='#1F1D36')

 import mysql.connector
 mydb= mysql.connector.connect(
    host='localhost',
    user='root',
    password='hassan543',
    port='3306',
    database='semproj'
    )
 def policy_add():
    cur = mydb.cursor()
    t = (pn_entry.get(), pt_entry.get(), pp_entry.get(), sa_entry.get(), tp_entry.get())

    s = 'INSERT INTO policy_edit values(%s,%s,%s,%s,%s)'
    cur.execute(s, t)
    pn_entry.delete(0, END)
    pt_entry.delete(0, END)
    pp_entry.delete(0, END)
    sa_entry.delete(0, END)
    tp_entry.delete(0, END)
    mydb.commit()
 #Canvas
 can = Canvas(hex, width=203, height=1090, bg='#3F3351', )
 can.place(x=0, y=0)
 can2 = Canvas(hex, width=1200, height=100, bg='#3F3351')
 can2.place(x=205, y=0)


 #LABLE FRONT PAGE
 norm = Font(family="Verdana", size=15, weight="bold", slant="italic")
 norm1 = Font(family="Verdana", size=20, weight="bold", slant="italic")
 norm2 = Font(family="Verdana", size=10, weight="bold", slant="italic")
 text1 = Label(hex, text="IMS", font=norm1, bg='#3F3351', fg='#EDEDED')
 text1.place(x=220, y=20)
 text = Label(hex, text="Insurance Management System.", font=norm, bg='#3F3351', fg='#EDEDED')
 text.place(x=220, y=50)
 text1 = Label(hex, text="Add Policy.", font=norm1, bg='#3F3351', fg='#EDEDED')
 text1.place(x=790, y=30)

 #EXIT BUTTON
 exit_btn = Button(hex, text="Exit", width=13, bg='#EDEDED', command=hex.quit)
 exit_btn.place(x=50, y=590)


 #ENTRIES LABLES FOR ADD POLICY
 tp_label = Label(hex, text="Policy Type:", fg='#EDEDED', bg='#1F1D36', font=norm2)
 tp_label.place(x=250, y=200)
 tp_entry = Entry(hex, width=40)
 tp_entry.place(x=350, y=200, height=25)

 pn_label = Label(hex, text="Policy Name:", fg='#EDEDED', bg='#1F1D36', font=norm2)
 pn_label.place(x=650, y=200)
 pn_entry = Entry(hex, width=40)
 pn_entry.place(x=750, y=200, height=25)

 pt_label = Label(hex, text="Policy Tenure:", fg='#EDEDED', bg='#1F1D36', font=norm2)
 pt_label.place(x=250, y=350)
 pt_entry = Entry(hex, width=40)
 pt_entry.place(x=360, y=350, height=25)

 pp_label = Label(hex, text="Policy Tenure:", fg='#EDEDED', bg='#1F1D36', font=norm2)
 pp_label.place(x=650, y=350)
 pp_entry = Entry(hex, width=40)
 pp_entry.place(x=760, y=350, height=25)

 sa_label = Label(hex, text="Sum Assurance:", fg='#EDEDED', bg='#1F1D36', font=norm2)
 sa_label.place(x=420, y=490)
 sa_entry = Entry(hex, width=40)
 sa_entry.place(x=545, y=490, height=25)

 #SUBMIT BUTTON
 submit_button_policy_add = Button(hex, text="Submit", width=13, bg='#EDEDED', command=policy_add)
 submit_button_policy_add.place(x=950, y=590)

 def onbutton(e):
    dashboard_button['bg'] = '#1F1D36'
 def leavebutton(e):
    dashboard_button['bg'] = '#3F3351'

 #DASHBOARD BUTTON
 dashboard_button = Button(hex, text="Dashboard", width=10, bg='#3F3351', fg='#EDEDED', font=norm1, borderwidth=0,
                         command=adminfront)
 dashboard_button.place(x=4, y=250)
 dashboard_button.bind('<Enter>', onbutton)
 dashboard_button.bind('<Leave>', leavebutton)



 hex.mainloop()
