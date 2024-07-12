import random
from tkinter import *
from tkinter import Button

root = Tk()
root.title("Game")
root.geometry('1070x200')

lbl0 = Label(root, text=10)
lbl0.grid(column=0, row=0, padx=10)

lbl1 = Label(root, text=9)
lbl1.grid(column=1, row=0, padx=10)

lbl2 = Label(root, text=8)
lbl2.grid(column=2, row=0, padx=10)

lbl3 = Label(root, text=7)
lbl3.grid(column=3, row=0, padx=10)

lbl4 = Label(root, text=6)
lbl4.grid(column=4, row=0, padx=10)

lbl5 = Label(root, text=5)
lbl5.grid(column=5, row=0, padx=10)

lbl6 = Label(root, text=4)
lbl6.grid(column=6, row=0, padx=10)

lbl7 = Label(root, text=3)
lbl7.grid(column=7, row=0, padx=10)

lbl8 = Label(root, text=2)
lbl8.grid(column=8, row=0, padx=10)

lbl9 = Label(root, text=1)
lbl9.grid(column=9, row=0, padx=10)

lbl10 = Label(root, text=0, fg='red')
lbl10.grid(column=10, row=0, padx=10)

lbl11 = Label(root, text=1)
lbl11.grid(column=11, row=0, padx=10)

lbl12 = Label(root, text=2)
lbl12.grid(column=12, row=0, padx=10)

lbl13 = Label(root, text=3)
lbl13.grid(column=13, row=0, padx=10)

lbl14 = Label(root, text=4)
lbl14.grid(column=14, row=0, padx=10)

lbl15 = Label(root, text=5)
lbl15.grid(column=15, row=0, padx=10)

lbl16 = Label(root, text=6)
lbl16.grid(column=16, row=0, padx=10)

lbl17 = Label(root, text=7)
lbl17.grid(column=17, row=0, padx=10)

lbl18 = Label(root, text=8)
lbl18.grid(column=18, row=0, padx=10)

lbl19 = Label(root, text=9)
lbl19.grid(column=19, row=0, padx=10)

lbl20 = Label(root, text=10)
lbl20.grid(column=20, row=0, padx=10)

btn0 = Button(root, bg='red', )
btn0.grid(column=0, row=1, padx=10, pady=8)

btn1 = Button(root, bg='red', )
btn1.grid(column=1, row=1, padx=10, pady=8)

btn2 = Button(root, bg='red', )
btn2.grid(column=2, row=1, padx=10, pady=8)

btn3 = Button(root, bg='red', )
btn3.grid(column=3, row=1, padx=10, pady=8)

btn4 = Button(root, bg='red', )
btn4.grid(column=4, row=1, padx=10, pady=8)

btn5 = Button(root, bg='red', )
btn5.grid(column=5, row=1, padx=10, pady=8)

btn6 = Button(root, bg='red', )
btn6.grid(column=6, row=1, padx=10, pady=8)

btn7 = Button(root, bg='red', )
btn7.grid(column=7, row=1, padx=10, pady=8)

btn8 = Button(root, bg='red', )
btn8.grid(column=8, row=1, padx=10, pady=8)

btn9 = Button(root, bg='red', )
btn9.grid(column=9, row=1, padx=10, pady=8)

btn10 = Button(root, bg='red', )
btn10.grid(column=10, row=1, padx=10, pady=8)

btn11 = Button(root, bg='red', )
btn11.grid(column=11, row=1, padx=10, pady=8)

btn12 = Button(root, bg='red', )
btn12.grid(column=12, row=1, padx=10, pady=8)

btn13 = Button(root, bg='red', )
btn13.grid(column=13, row=1, padx=10, pady=8)

btn14 = Button(root, bg='red', )
btn14.grid(column=14, row=1, padx=10, pady=8)

btn15 = Button(root, bg='red', )
btn15.grid(column=15, row=1, padx=10, pady=8)

btn16 = Button(root, bg='red', )
btn16.grid(column=16, row=1, padx=10, pady=8)

btn17 = Button(root, bg='red', )
btn17.grid(column=17, row=1, padx=10, pady=8)

btn18 = Button(root, bg='red', )
btn18.grid(column=18, row=1, padx=10, pady=8)

btn19 = Button(root, bg='red', )
btn19.grid(column=19, row=1, padx=10, pady=8)

btn20 = Button(root, bg='red', )
btn20.grid(column=20, row=1, padx=10, pady=8)

list1 = [1, 2, 3, 4, 5, 6]

list2 = [1, 2, 3, 4, 5, 6]

scr1 = Label(root, text="0")
scr1.grid(row=4, column=0, padx=10, pady=7)

scr2 = Label(root, text="0")
scr2.grid(row=4, column=20, padx=10, pady=7)

ran1 = 0
ran2 = 0

btnlist = [btn0, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16,
           btn17, btn18, btn19, btn20, btn20]

keep = 10
btn = 0
old_keep = 0


def clicked1():
    global ran1
    global keep
    global btn
    global old_keep
    old_keep = keep
    keep = keep - ran1
    if keep < 0:
        keep = keep + ran1
    ran1 = random.choice(list1)
    scr1.configure(text=ran1)
    btn = btnlist[old_keep]
    btn.configure(bg='red')
    btn = btnlist[keep]
    btn.configure(bg='green')


def clicked2():
    global ran2
    global keep
    global btn
    global old_keep
    old_keep = keep
    keep = keep + ran2
    if keep > 20:
        keep = keep - ran2
    ran2 = random.choice(list2)
    scr2.configure(text=ran2)
    btn = btnlist[old_keep]
    btn.configure(bg='red')
    btn = btnlist[keep]
    btn.configure(bg='green')


btnp1 = Button(root, text="Player-1", command=clicked1)
btnp1.grid(row=3, column=0, padx=0, pady=8)

btnp2 = Button(root, text="Player-2", command=clicked2)
btnp2.grid(row=3, column=20, padx=0, pady=8)


# btnlist = [btn0, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16
# , btn17, btn18, btn19, btn20, btn20]

# btnp1.configure(command=lambda: [score(), clicked1()])
# btnp2.configure(command=lambda: [clicked2(), score()])

root.mainloop()
