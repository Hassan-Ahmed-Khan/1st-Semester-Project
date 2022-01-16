
from tkinter import *




def Customerfront():
    from PIL import Image, ImageTk
    from tkinter import filedialog
    import messagebox
    from tkinter import Tk
    from tkinter import Canvas
    from tkinter import Button
    from tkinter import Label
    from tkinter.font import Font
    cf = Tk()
    cf.title("Customer")
    cf.geometry("1090x660")
    cf.configure(bg='#1F1D36')
    cf.iconbitmap('E:/UNI/1st semester projett/pics/img1.png')
    cf.state('zoomed')
    norm = Font(family="Verdana", size=15, weight="bold", slant="italic")
    norm1 = Font(family="Verdana", size=20, weight="bold", slant="italic")
    norm3 = Font(family="Verdana", size=9, weight="bold", slant="italic")


    def viewpolicy():
        # TKINTER LIBRARY
        cf.destroy()
        from tkinter import Tk
        from tkinter import Canvas
        from tkinter import Button
        from tkinter import Entry
        from tkinter import Label
        from tkinter.font import Font
        sda = Tk()
        sda.title("View/Edit Policy")
        sda.geometry("1300x660")
        sda.configure(bg='#1F1D36')
        sda.resizable(0, 0)
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


        #Apply function
        def apply():

                ask = messagebox.askyesno(title='Confirmation', message="Do you want to apply for the following policy")

                def userS():
                    # Tkinter library import
                    from tkinter import END
                    from tkinter.font import Font
                    from tkinter import Tk
                    from tkinter import Canvas
                    from tkinter import Button
                    from tkinter import Entry
                    from tkinter import Label
                    topo = Tk()
                    topo.title("User Signup")
                    topo.geometry("400x200")
                    topo.configure(bg='#064663')
                    topo.resizable(0,0)
                    # Database connection
                    import mysql.connector
                    mydb = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='hassan543',
                        port='3306',
                        database='semproj'
                    )

                    # user entry boxex
                    hlabel = Label(topo, text="Confirm information for submission:", bg='#064663', fg='#B4C6A6')
                    hlabel.grid(row=1, column=0)
                    f_n = Entry(topo, width=30)
                    f_n.grid(row=3, column=1, pady=5, padx=5)
                    a_d = Entry(topo, width=30)
                    a_d.grid(row=4, column=1, pady=5, padx=5)

                    # user entry boxes titles
                    f_n_label = Label(topo, text="Full name:", bg='#064663', fg='#B4C6A6')
                    f_n_label.place(x=3, y=20)
                    a_d_label = Label(topo, text="Email:", bg='#064663', fg='#B4C6A6')
                    a_d_label.place(x=3, y=40)

                    # Insert function
                    def insertS():
                        cur = mydb.cursor()
                        t = (f_n.get(), a_d.get())
                        cur.execute('INSERT INTO policy_holders values(%s,%s)', t)
                        f_n.delete(0, END)
                        a_d.delete(0, END)
                        mydb.commit()
                        topo.destroy()


                    # Submit button
                    sub_btn = Button(topo, text="Submit", bg='#B4C6A6', width=10, command=insertS)
                    sub_btn.place(x=210, y=100)

                    topo.mainloop()
                userS()




        num1 = 180
        n = 1


        for i in table:
            l12 = Button (sda, text="Apply", font=norm3, bg='#87AAAA', fg='#EDEDED', command=apply)
            l12.place(x=1230, y=num1)
            l11 = Label(sda, text=n, font=norm3, bg='#1F1D36', fg='#EDEDED')
            l11.place(x=230, y=num1)
            n  = n + 1
            policy_name = Label(sda, text=i[0], font=norm2, fg='#87AAAA', bg='#1F1D36')
            policy_name.place(x=250, y=num1)

            policy_Premium = Label(sda, text=i[1], font=norm2, fg='#87AAAA', bg='#1F1D36')
            policy_Premium.place(x=450, y=num1)

            policy_tenure = Label(sda, text=i[2], font=norm2, fg='#87AAAA', bg='#1F1D36')
            policy_tenure.place(x=650, y=num1)

            policy_sum = Label(sda, text=i[3], font=norm2, fg='#87AAAA', bg='#1F1D36')
            policy_sum.place(x=850, y=num1)

            policy_type = Label(sda, text=i[4], font=norm2, fg='#87AAAA', bg='#1F1D36')
            policy_type.place(x=1050, y=num1)

            num1 = num1 + 30

        # CANVAS STUFF

        can = Canvas(sda, width=203, height=1090, bg='#3F3351', )
        can.place(x=0, y=0)
        can2 = Canvas(sda, width=1200, height=100, bg='#3F3351')
        can2.place(x=205, y=0)

        # LABLE FRONT PAGE
        text1 = Label(sda, text="IMS", font=norm1, bg='#3F3351', fg='#EDEDED')
        text1.place(x=220, y=20)
        text = Label(sda, text="Insurance Management System.", font=norm, bg='#3F3351', fg='#EDEDED')
        text.place(x=220, y=50)
        text1 = Label(sda, text="Apply Policy.", font=norm1, bg='#3F3351', fg='#EDEDED')
        text1.place(x=790, y=30)

        # exit button
        exit_btn = Button(sda, text="Exit", width=13, bg='#EDEDED', command=sda.quit)
        exit_btn.place(x=50, y=590)

        # DASHBOARD BUTTON
        def comb1():
            sda.destroy()
            Customerfront()

        dashboard_button = Button(sda, text="Dashboard", width=10, bg='#3F3351', fg='#EDEDED', font=norm1, borderwidth=0,
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



        # ENTRIES LABLES FOR ADD POLICY
        tpp_label = Label(sda, text="Policy Name", fg='#EDEDED', bg='#1F1D36', font=norm2)
        tpp_label.place(x=250, y=150)

        pnn_label = Label(sda, text="Policy Premimum", fg='#EDEDED', bg='#1F1D36', font=norm2)
        pnn_label.place(x=450, y=150)

        ptt_label = Label(sda, text="Policy Tenure", fg='#EDEDED', bg='#1F1D36', font=norm2)
        ptt_label.place(x=650, y=150)

        ppp_label = Label(sda, text="Sum Assurance", fg='#EDEDED', bg='#1F1D36', font=norm2)
        ppp_label.place(x=850, y=150)

        saa_label = Label(sda, text="Policy Type", fg='#EDEDED', bg='#1F1D36', font=norm2)
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

        sda.mainloop()
    def pe():
        level.destroy()
        from tkinter import END
        from tkinter.font import Font
        from tkinter import Tk
        from tkinter import Canvas
        from tkinter import Button
        from tkinter import Entry
        from tkinter import Label

        hex = Tk()
        hex.title("Policy Add")
        hex.geometry("1090x660")
        hex.resizable(0, 0)
        hex.configure(bg='#1F1D36')

        import mysql.connector
        mydb = mysql.connector.connect(
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

        # Canvas
        can = Canvas(hex, width=203, height=1090, bg='#3F3351', )
        can.place(x=0, y=0)
        can2 = Canvas(hex, width=1200, height=100, bg='#3F3351')
        can2.place(x=205, y=0)

        # LABLE FRONT PAGE
        norm = Font(family="Verdana", size=15, weight="bold", slant="italic")
        norm1 = Font(family="Verdana", size=20, weight="bold", slant="italic")
        norm2 = Font(family="Verdana", size=10, weight="bold", slant="italic")
        text1 = Label(hex, text="IMS", font=norm1, bg='#3F3351', fg='#EDEDED')
        text1.place(x=220, y=20)
        text = Label(hex, text="Insurance Management System.", font=norm, bg='#3F3351', fg='#EDEDED')
        text.place(x=220, y=50)
        text1 = Label(hex, text="Add Policy.", font=norm1, bg='#3F3351', fg='#EDEDED')
        text1.place(x=790, y=30)

        # EXIT BUTTON
        exit_btn = Button(hex, text="Exit", width=13, bg='#EDEDED', command=hex.destroy)
        exit_btn.place(x=50, y=590)

        # ENTRIES LABLES FOR ADD POLICY
        tp_label = Label(hex, text="Policy Type:", fg='#EDEDED', bg='#1F1D36', font=norm2)
        tp_label.place(x=250, y=200)
        tp_entry = Entry(hex, width=40)
        tp_entry.place(x=350, y=200, height=25)

        pn_label = Label(hex, text="Policy Name:", fg='#EDEDED', bg='#1F1D36', font=norm2)
        pn_label.place(x=650, y=200)
        pn_entry = Entry(hex, width=40)
        pn_entry.place(x=750, y=200, height=25)

        pt_label = Label(hex, text="Policy Premimum:", fg='#EDEDED', bg='#1F1D36', font=norm2)
        pt_label.place(x=230, y=350)
        pt_entry = Entry(hex, width=40)
        pt_entry.place(x=370, y=350, height=25)

        pp_label = Label(hex, text="Policy Tenure:", fg='#EDEDED', bg='#1F1D36', font=norm2)
        pp_label.place(x=650, y=350)
        pp_entry = Entry(hex, width=40)
        pp_entry.place(x=760, y=350, height=25)

        sa_label = Label(hex, text="Sum Assurance:", fg='#EDEDED', bg='#1F1D36', font=norm2)
        sa_label.place(x=420, y=490)
        sa_entry = Entry(hex, width=40)
        sa_entry.place(x=545, y=490, height=25)

        # SUBMIT BUTTON
        submit_button_policy_add = Button(hex, text="Submit", width=13, bg='#EDEDED', command=policy_add)
        submit_button_policy_add.place(x=950, y=590)

        def comb():
             hex.destroy()
             adminfront()

        # DASHBOARD BUTTON
        dashboard_button = Button(hex, text="Dashboard", width=10, bg='#3F3351', fg='#EDEDED', font=norm1,
                                  borderwidth=0, command=comb)
        dashboard_button.place(x=4, y=250)
        def onbutton(e):
            dashboard_button['bg'] = '#1F1D36'

        def leavebutton(e):
            dashboard_button['bg'] = '#3F3351'

        dashboard_button.bind('<Enter>', onbutton)
        dashboard_button.bind('<Leave>', leavebutton)

        hex.mainloop()

    # Canvas

    can = Canvas(cf, width=203, height=1090, bg='#3F3351', )
    can.place(x=0, y=0)
    can2 = Canvas(cf, width=1200, height=100, bg='#3F3351')
    can2.place(x=205, y=0)


    def imgcomb():
        cf.filename = filedialog.askopenfile(initialdir='//c', filetypes=(("png files", "*.png"),("all files", "*.*")))
        img1 = Label(cf, image=cf.filename)
        img1.place(x=400, y=400)
     # DASHBOARD BUTTON
    img_button = Button(cf, text="Select Image", width=13, bg='#3F3351', fg='#EDEDED', font=norm3,
                              borderwidth=0, command=imgcomb)
    img_button.place(x=39, y=150)

    def onbutton(e):
        img_button['bg'] = '#1F1D36'

    def leavebutton(e):
        img_button['bg'] = '#3F3351'

    img_button.bind('<Enter>', onbutton)
    img_button.bind('<Leave>', leavebutton)

    # LABLE FRONT PAGE

    text1 = Label(cf, text="IMS", font=norm1, bg='#3F3351', fg='#EDEDED')
    text1.place(x=220, y=20)
    text = Label(cf, text="Insurance Management System.", font=norm, bg='#3F3351', fg='#EDEDED')
    text.place(x=220, y=50)
    text1 = Label(cf, text="User Account.", font=norm1, bg='#3F3351', fg='#EDEDED')
    text1.place(x=1080, y=30)

    # EXIT BUTTON
    exit_btn = Button(cf, text="Exit", width=13, bg='#EDEDED', command=cf.quit)
    exit_btn.place(x=50, y=660)

    # APPLY POLICY BUTTON FUNCTION

    # APPLY POLICY BUTTON
    ap_btn = Button(cf, text="Apply Policy", font=norm, width=17, bg='#79B4B7', fg='#EDEDED', command=viewpolicy)
    ap_btn.place(x=300, y=180, height=130)







    # VIEW/EDIT POLICY BUTTON
    ep_btn = Button(cf, text="Applied Policy", font=norm, width=17, bg='#79B4B7', fg='#EDEDED', command=viewpolicy)
    ep_btn.place(x=640, y=180, height=130)

    # POLICY HOLDERS BUTTON
    ph_btn = Button(cf, text="Log out", font=norm, width=17, bg='#79B4B7', fg='#EDEDED', command=cf.quit)
    ph_btn.place(x=1000, y=180, height=130)


    cf.mainloop()
Customerfront()