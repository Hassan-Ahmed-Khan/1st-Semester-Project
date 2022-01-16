
def userS():
 #Tkinter library import
 from tkinter import END
 from tkinter.font import Font
 from tkinter import Tk
 from tkinter import Canvas
 from tkinter import Button
 from tkinter import Entry
 from tkinter import Label
 top = Tk()
 top.title("User Signup")
 top.geometry("400x400")
 top.configure(bg='#064663')

 #Database connection
 import mysql.connector
 mydb = mysql.connector.connect(
   host='localhost',
   user='root',
   password='hassan543',
   port='3306',
   database='semproj'
 )

 #user entry boxex
 f_n = Entry(top, width=30)
 f_n.grid(row=1, column=1, pady=20, padx=20)
 a_d = Entry(top, width=30)
 a_d.grid(row=2, column=1, pady=20, padx=20)
 p_s = Entry(top, width=30)
 p_s.grid(row=3, column=1, pady=20, padx=20)
 m_n = Entry(top, width=30)
 m_n.grid(row=4, column=1, pady=20, padx=20)
 e_m = Entry(top, width=30)
 e_m.grid(row=5, column=1, pady=20, padx=20)

 #user entry boxes titles
 f_n_label = Label(top, text="Full name:", bg='#064663', fg='#B4C6A6')
 f_n_label.grid(row=1, column=0, padx=20)
 a_d_label = Label(top, text="Address:", bg='#064663', fg='#B4C6A6')
 a_d_label.grid(row=2, column=0, padx=20)
 p_s_label = Label(top, text="Password:", bg='#064663', fg='#B4C6A6')
 p_s_label.grid(row=3, column=0, padx=20)
 m_n_label = Label(top, text="Mobile no:", bg='#064663', fg='#B4C6A6')
 m_n_label.grid(row=4, column=0, padx=20)
 e_m_label = Label(top, text="Email:", bg='#064663', fg='#B4C6A6')
 e_m_label.grid(row=5, column=0, padx=20)


 # Insert function
 def insertS():
  cur = mydb.cursor()
  t = (f_n.get(), a_d.get(), p_s.get(), m_n.get(), e_m.get())
  cur.execute('INSERT INTO signup values(%s,%s,%s,%s,%s)', t)
  f_n.delete(0, END)
  a_d.delete(0, END)
  p_s.delete(0, END)
  m_n.delete(0, END)
  top.destroy()
  mydb.commit()

 #Submit button
 sub_btn=Button(top, text="Submit", bg='#B4C6A6', width=10 , command=insertS)
 sub_btn.place(x=160, y=330)

 top.mainloop()
userS()


