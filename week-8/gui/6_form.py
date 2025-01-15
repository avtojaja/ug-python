from tkinter import *

def display_fullname():
    print(firstname.get() + ' ' + lastname.get())

root = Tk()
Label(root, text='First Name').grid(row=0)
Label(root, text='Last Name').grid(row=1)
firstname = Entry(root)
lastname = Entry(root)
firstname.grid(row=0, column=1)
lastname.grid(row=1, column=1)

button = Button(root, text='Fullname', width=25, command=display_fullname)
button.grid(row=3, column=0)

root.mainloop()
