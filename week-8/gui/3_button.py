import tkinter as tk

root = tk.Tk()
root.title('Python Course')
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()

root.mainloop()
