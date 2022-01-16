from tkinter import *
root = Tk()
root.title("Calculator App")
e= Entry(root, borderwidth=4, width=50 )
e.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
def add():
    return


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: add)
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: add)
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: add)
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: add)
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: add)
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: add)
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: add)
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: add)
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: add)
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: add)
button_clear = Button(root, text="clear",padx=101, pady=20, command=add)
button_equal = Button(root, text="=", padx=39, pady=20,command=add)
button_add = Button(root, text="+", padx=110, pady=20,command=add)
button_1.grid(row=3, column=3)
button_2.grid(row=3, column=2)
button_3.grid(row=3, column=1)
button_4.grid(row=2, column=3)
button_5.grid(row=2, column=2)
button_6.grid(row=2, column=1)
button_7.grid(row=1, column=3)
button_8.grid(row=1, column=2)
button_9.grid(row=1, column=1)
button_0.grid(row=4, column=1)
button_clear.grid(row=4, column=2, columnspan=2)
button_add.grid(row=5, column=2, columnspan=2)
button_equal.grid(row=5, column=1)
root.mainloop()



def signup():
 first_name = input("First name: ")
 last_name = input("Last name: ")
 address = input("Address: ")
 password = input("Password: ")
 mob_no = input("Mobile no.: ")
