from tkinter import *

def select():
    monitor.config(text="{}".format(option.get()))
def reset():
    option.set(None)
    monitor.config(text="")

root = Tk()
option = StringVar()
option.set(None)
Radiobutton(root, text="Java", variable=option, 
            value='Java', command=select).pack(anchor=W)
Radiobutton(root, text="C++", variable=option, 
            value='C++', command=select).pack(anchor=W)
Radiobutton(root, text="C#", variable=option,   
            value='C#', command=select).pack(anchor=W)
Radiobutton(root, text="Python", variable=option,   
            value='Python', command=select).pack(anchor=W)

monitor = Label(root)
monitor.pack()
Button(root, text="Reiniciar", command=reset).pack()

root.mainloop()