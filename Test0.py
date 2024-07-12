from tkinter import *

root = Tk()
root.title("Hi")
root.geometry('360x70')

menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

lbl = Label(root, text="Hi, I am Samyak, do you like me?")
lbl.grid(row=0, column=0)
txt = Entry(root, width=10)
txt.grid(row=0, column=1)

def clicked():
    lbl.configure(text="You wrote "+txt.get())

btn = Button(root, text="Click me", fg="red", command=clicked)
btn.grid(column=2, row=0)


root.mainloop()
