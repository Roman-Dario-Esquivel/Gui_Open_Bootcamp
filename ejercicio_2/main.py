from tkinter import *
screen_aux = Tk()
elemento = StringVar()
listbox = Listbox(screen_aux)
lis = ["angular", "boostrap", "javascript", "java", "spring", "git", "github", "mysql","postman","xampp","C#"]
for item in lis:
 listbox.insert(END, item)
listbox.pack()
label = Label(text="Lista de programas y heeramientas usadas")
label.pack()
screen_aux.mainloop()
