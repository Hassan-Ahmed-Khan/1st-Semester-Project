# Tkinter library import
from tkinter import *

import Image
import ImageTk


def frontpage():
    from tkinter import messagebox
    from tkinter import END
    from tkinter.font import Font
    from tkinter import Tk
    from tkinter import Canvas
    from tkinter import Button
    from tkinter import Entry
    from tkinter import Label
    from operator import itemgetter
    from tkinter.font import Font
    from PIL import Image,ImageTk



    #FRONT PAGE WINDOW ROOT
    root = Tk()
    root.title("IMS")
    root.geometry("1100x630")
    root.resizable(0, 0)
    #IMG1
    bg = PhotoImage(file="E:/UNI/1st semester projett/pics/bg.png")
    img = Label(root, image=bg)
    img.place(x=0, y=0, relwidth=1, relheight=1)
    #IMG2
    bgg = PhotoImage(file="E:/UNI/1st semester projett/pics/bg2.png")
    img1 = Label(root, image=bgg, bg="#95D1CC")
    img1.place(x=100, y=80)
#Main functions ADMIN AND CUSTOMERS
    def Customerfront():
        root.destroy()
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

            # Apply function
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
                    topo.resizable(0, 0)
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
                l12 = Button(sda, text="Apply", font=norm3, bg='#87AAAA', fg='#EDEDED', command=apply)
                l12.place(x=1230, y=num1)
                l11 = Label(sda, text=n, font=norm3, bg='#1F1D36', fg='#EDEDED')
                l11.place(x=230, y=num1)
                n = n + 1
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
                sda.destroy
                Customerfront()

            dashboard_button = Button(sda, text="Dashboard", width=10, bg='#3F3351', fg='#EDEDED', font=norm1,
                                      borderwidth=0,
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
        ap_btn = Button(cf, text="Apply Policy", font=norm, width=30, bg='#79B4B7', fg='#EDEDED', command=viewpolicy)
        ap_btn.place(x=300, y=180, height=130)

        # POLICY HOLDERS BUTTON
        ph_btn = Button(cf, text="Log out", font=norm, width=30, bg='#79B4B7', fg='#EDEDED', command=cf.quit)
        ph_btn.place(x=800, y=180, height=130)

        cf.mainloop()


    def adminfront():
        root.destroy()
        from tkinter import Image, PhotoImage
        from tkinter import Tk
        from tkinter import Canvas
        from tkinter import Button
        from tkinter import Label
        from tkinter.font import Font
        level = Tk()
        level.title("Admin")
        level.geometry("1090x660")
        level.configure(bg='#1F1D36')
        level.iconbitmap('E:/UNI/1st semester projett/pics/img1.png')
        level.state('zoomed')

        bgg3 = PhotoImage(file="E:/UNI/1st semester projett/pics/bg3.png")
        img3 = Label(level, image=bgg3, bg="#95D1CC")
        img3.place(x=0, y=0)

        def registeredusers():
            # TKINTER LIBRARY
            level.destroy()
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
            text = Label(sv, text="Insurance Management System.", font=norm, bg='#3F3351',
                         fg='#EDEDED')
            text.place(x=220, y=50)
            text1 = Label(sv, text="Registered Users.", font=norm1, bg='#3F3351', fg='#EDEDED')
            text1.place(x=890, y=30)

            # exit button
            exit_btn = Button(sv, text="Exit", width=13, bg='#EDEDED', command=sv.quit)
            exit_btn.place(x=50, y=590)

            # DASHBOARD BUTTON
            def comb2():
                sv.destroy
                adminfront()

            dashboard_button = Button(sv, text="Dashboard", width=10, bg='#3F3351', fg='#EDEDED',
                                      font=norm1, borderwidth=0,
                                      command=comb2)
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

        def viewpolicy():
            # TKINTER LIBRARY
            level.destroy()
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
            text = Label(sd, text="Insurance Management System.", font=norm, bg='#3F3351',
                         fg='#EDEDED')
            text.place(x=220, y=50)
            text1 = Label(sd, text="Policy View/Edit.", font=norm1, bg='#3F3351', fg='#EDEDED')
            text1.place(x=790, y=30)

            # exit button
            exit_btn = Button(sd, text="Exit", width=13, bg='#EDEDED', command=sd.quit)
            exit_btn.place(x=50, y=590)

            # DASHBOARD BUTTON
            def comb1():

                adminfront()
                sd.destroy

            dashboard_button = Button(sd, text="Dashboard", width=10, bg='#3F3351', fg='#EDEDED',
                                      font=norm1, borderwidth=0,
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



            sd.mainloop()

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
            text = Label(hex, text="Insurance Management System.", font=norm, bg='#3F3351',
                         fg='#EDEDED')
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

            pp_label = Label(hex, text="(in months)", fg='#EDEDED', bg='#1F1D36', font=norm2)
            pp_label.place(x=650, y=375)

            sa_label = Label(hex, text="Sum Assurance:", fg='#EDEDED', bg='#1F1D36', font=norm2)
            sa_label.place(x=420, y=490)
            sa_entry = Entry(hex, width=40)
            sa_entry.place(x=545, y=490, height=25)

            # SUBMIT BUTTON
            submit_button_policy_add = Button(hex, text="Submit", width=13, bg='#EDEDED',
                                              command=policy_add)
            submit_button_policy_add.place(x=950, y=590)

            def comb():
                hex.destroy
                adminfront()

            # DASHBOARD BUTTON
            dashboard_button = Button(hex, text="Dashboard", width=10, bg='#3F3351', fg='#EDEDED',
                                      font=norm1,
                                      borderwidth=0, command=comb)
            dashboard_button.place(x=4, y=250)

            def onbutton(e):
                dashboard_button['bg'] = '#1F1D36'

            def leavebutton(e):
                dashboard_button['bg'] = '#3F3351'

            dashboard_button.bind('<Enter>', onbutton)
            dashboard_button.bind('<Leave>', leavebutton)

            hex.mainloop()

        def ph():
            # TKINTER LIBRARY
            level.destroy()
            from tkinter import Tk
            from tkinter import Canvas
            from tkinter import Button
            from tkinter import Entry
            from tkinter import Label
            from tkinter.font import Font
            sde = Tk()
            sde.title("View/Edit Policy")
            sde.geometry("1300x660")
            sde.configure(bg='#1F1D36')
            sde.resizable(0, 0)
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
            cur.execute('SELECT * FROM policy_holders')
            table = cur.fetchall()
            num1 = 180
            n = 1
            for i in table:
                l11 = Label(sde, text=n, font=norm3, bg='#1F1D36', fg='#EDEDED')
                l11.place(x=230, y=num1)
                n = n + 1
                full_name = Label(sde, text=i[0], font=norm2, fg='#87AAAA', bg='#1F1D36')
                full_name.place(x=250, y=num1)

                email_Premium = Label(sde, text=i[1], font=norm2, fg='#87AAAA', bg='#1F1D36')
                email_Premium.place(x=450, y=num1)

                num1 = num1 + 30

            # CANVAS STUFF
            can = Canvas(sde, width=203, height=1090, bg='#3F3351', )
            can.place(x=0, y=0)
            can2 = Canvas(sde, width=1200, height=100, bg='#3F3351')
            can2.place(x=205, y=0)

            # LABLE FRONT PAGE
            text1 = Label(sde, text="IMS", font=norm1, bg='#3F3351', fg='#EDEDED')
            text1.place(x=220, y=20)
            text = Label(sde, text="Insurance Management System.", font=norm, bg='#3F3351',
                         fg='#EDEDED')
            text.place(x=220, y=50)
            text1 = Label(sde, text="Policy View/Edit.", font=norm1, bg='#3F3351', fg='#EDEDED')
            text1.place(x=790, y=30)

            # exit button
            exit_btn = Button(sde, text="Exit", width=13, bg='#EDEDED', command=sde.quit)
            exit_btn.place(x=50, y=590)

            # DASHBOARD BUTTON
            def comb1():
                sde.destroy
                adminfront()

            dashboard_button = Button(sde, text="Dashboard", width=10, bg='#3F3351', fg='#EDEDED',
                                      font=norm1, borderwidth=0,
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
            tpp_label = Label(sde, text="Customer Full Name", fg='#EDEDED', bg='#1F1D36', font=norm2)
            tpp_label.place(x=250, y=150)

            pnn_label = Label(sde, text="Customer Email", fg='#EDEDED', bg='#1F1D36', font=norm2)
            pnn_label.place(x=450, y=150)

            sde.mainloop()

        # Canvas
        can = Canvas(level, width=203, height=1090, bg='#082032', )
        can.place(x=0, y=0)
        can2 = Canvas(level, width=1200, height=100, bg='#082032')
        can2.place(x=205, y=0)

        # LABLE FRONT PAGE
        norm = Font(family="Verdana", size=15, weight="bold", slant="italic")
        norm1 = Font(family="Verdana", size=20, weight="bold", slant="italic")
        text1 = Label(level, text="IMS", font=norm1, bg='#082032', fg='#EDEDED')
        text1.place(x=220, y=20)
        text = Label(level, text="Insurance Management System.", font=norm, bg='#082032',
                     fg='#EDEDED')
        text.place(x=220, y=50)
        text1 = Label(level, text="Admin Account.", font=norm1, bg='#082032', fg='#EDEDED')
        text1.place(x=1080, y=30)

        # EXIT BUTTON
        exit_btn = Button(level, text="Exit", width=13, bg='#EDEDED', command=level.destroy)
        exit_btn.place(x=50, y=660)

        # ADD NEW POLICY BUTTON
        np_btn = Button(level, text="Add New Policy", font=norm, width=17, bg='#79B4B7',
                        fg='#EDEDED', command=pe)
        np_btn.place(x=300, y=180, height=130)

        # VIEW/EDIT POLICY BUTTON
        ep_btn = Button(level, text="View/Edit Policy", font=norm, width=17, bg='#79B4B7',
                        fg='#EDEDED', command=viewpolicy)
        ep_btn.place(x=640, y=180, height=130)

        # POLICY HOLDERS BUTTON
        ph_btn = Button(level, text="Policy Holders", font=norm, width=17, bg='#79B4B7',
                        fg='#EDEDED', command=ph)
        ph_btn.place(x=1000, y=180, height=130)

        # REGISTERED USERS BUTTON
        r_btn = Button(level, text="Registered Users", font=norm, width=17, bg='#79B4B7',
                       fg='#EDEDED', command=registeredusers)
        r_btn.place(x=300, y=440, height=130)

        level.mainloop()

    #FUNCTION FOR USER SIGNUP DISPLAY
    def userS():
        top = Tk()
        top.title("User Signup")
        top.geometry("400x400")
        top.configure(bg='#064663')

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


        # user entry boxes titles
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

        # Insert function IN DATA BASE FOR USER SINUP
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

        # Submit button
        sub_btn = Button(top, text="Submit", bg='#B4C6A6', width=10, command=insertS)
        sub_btn.place(x=160, y=330)

        top.mainloop()
    #FUNCTION FOR ADMIN SIGNUP DISPLAY
    def adminS():
        top = Tk()
        top.title("User Signup")
        top.geometry("400x400")
        top.resizable(0, 0)
        top.configure(bg='#064663')

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

        # user entry boxes titles
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

        # Insert functionIN DATABSE FOR SIGNUP ADMIN
        def insertS():
            cur = mydb.cursor()
            t = (f_n.get(), a_d.get(), p_s.get(), m_n.get(), e_m.get())
            cur.execute('INSERT INTO adminsignup values(%s,%s,%s,%s,%s)', t)
            f_n.delete(0, END)
            a_d.delete(0, END)
            p_s.delete(0, END)
            m_n.delete(0, END)
            top.destroy()
            mydb.commit()

        # Submit button
        sub_btn = Button(top, text="Submit", bg='#B4C6A6', width=10, command=insertS)
        sub_btn.place(x=160, y=330)

        top.mainloop()

    norm = Font(family="Verdana", size=15, weight="bold", slant="italic")
    norm1 = Font(family="Verdana", size=20, weight="bold", slant="italic")
    norm2 = Font(family="Verdana", size=10, weight="bold", slant="italic")
    norm3 = Font(family="Verdana", size=7, weight="bold", slant="italic")

    #Admin Login button function
    def box():


        signup_label = Label(root, text="Login", font=norm, bg='#95D1CC', fg='#084177')
        signup_label.place(x=760, y=200)

        s1_label = Label(root, text="Email:", bg='#95D1CC', fg='#084177')
        s1_label.place(x=620, y=300)

        s1_entry=Entry(root, width=50)
        s1_entry.place(x=700, y=300, height=25)

        s2_label = Label(root, text="Password:", bg='#95D1CC', fg='#084177')
        s2_label.place(x=620, y=400)

        s2_entry = Entry(root, width=50, show="*")
        s2_entry.place(x=700, y=400, height=25)



        def check():
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
            cursor.execute("Select Email from adminsignup")
            cursor2.execute("Select Password from adminsignup")
            email = s1_entry.get()
            password = s2_entry.get()
            e = []
            p = []
            for i in cursor:
                e.append(i)
            for j in cursor2:
                p.append(j)
            res = list(map(itemgetter(0), e))
            res2 = list(map(itemgetter(0), p))
            k = len(res)
            i = 0

            while i < k:
                    if res[i] == email and res2[i] == password:

                        adminfront()
                        break
                    i += 1
            else:
              messagebox.showinfo(title="Error", message="Incorrect credentials")


        sub_btn = Button(root, text="Login", width=13, bg='#B4C6A6', command=check)
        sub_btn.place(x=700, y=500)

        sign_btn = Button(root, text="Signup", width=13, bg='#B4C6A6', command=adminS)
        sign_btn.place(x=850, y=500)

    # USER LOGIN BUTTON FUNCTION
    def box1():
        signup_label = Label(root, text="Login", font=norm, bg='#B4C6A6', fg='#084177')
        signup_label.place(x=760, y=200)

        s1_label = Label(root, text="Email:", bg='#B4C6A6', fg='#084177')
        s1_label.place(x=620, y=300)

        s11_entry = Entry(root, width=50)
        s11_entry.place(x=700, y=300, height=25)

        s2_label = Label(root, text="Password:", bg='#B4C6A6', fg='#084177')
        s2_label.place(x=620, y=400)

        s22_entry = Entry(root, width=50)
        s22_entry.place(x=700, y=400, height=25)

        def check1():
            from operator import itemgetter
            import mysql.connector

            mydbc = mysql.connector.connect(
                host='localhost',
                user='root',
                password='hassan543',
                port='3306',
                database='semproj'
            )
            cur1 = mydbc.cursor()
            import mysql.connector

            mydba = mysql.connector.connect(
                host='localhost',
                user='root',
                password='hassan543',
                port='3306',
                database='semproj'
            )
            cur2 = mydba.cursor()

            sql_command1 = "Select Email from signup"
            sql_command2 = "Select Password from signup"
            cur1.execute("Select Email from signup")
            cur2.execute("Select Password from signup")
            email = s11_entry.get()
            password = s22_entry.get()
            em = []
            pas = []
            for i in cur1:
                em.append(i)
            for j in cur2:
                pas.append(j)
            res1 = list(map(itemgetter(0), em))
            res3 = list(map(itemgetter(0), pas))
            k = len(res1)
            i = 1

            while i < k:
                if res1[i] == email and res3[i] == password:
                    Customerfront()
                    break
                i+=1

            else:

                 messagebox.showinfo(title="Unsuccessful", message="Login Unsuccessful")




        sub_btn = Button(root, text="Login", width=13, bg='#B4C6A6', command=check1)
        sub_btn.place(x=700, y=500)

        sign_btn = Button(root, text="Signup", width=13, bg='#B4C6A6', command=userS)
        sign_btn.place(x=850, y=500)

    # BUTTON ADMIN
    btn_ad = Button(root, text="Admin", width=13, bg='#B4C6A6', command=box)
    btn_ad.place(x=700, y=50)



    # BUTTON USER
    btn_us = Button(root, text="User ", width=13, bg='#B4C6A6', command=box1)
    btn_us.place(x=850, y=50)

    root.mainloop()
frontpage()