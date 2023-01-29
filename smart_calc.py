import tkinter
from tkinter import *
import re

mul_text=['multiply', '*', 'x', 'multiplication']
div_text=['division', '/', 'divide','div']
add_text=['add', '+', 'addition', 'sum']
sub_text=['subtract', '-', 'minus', 'subtraction', 'difference']


def number_extract():
    nums=re.findall('\d+' ,problem.get())
    return nums

def operation():
    muldiv=1
    addsub=0
    numbers = number_extract()
    if any(a in problem.get().lower() for a in mul_text):
        for i in numbers:
            muldiv*=int(i)
        lb.delete(0, END)
        lb.insert(END, addsub)
    elif any(a in problem.get().lower() for a in div_text):
        for i in numbers:
            addsub=int(numbers[0])-int(numbers[1])
        lb.delete(0, END)
        lb.insert(END, addsub)
    elif any(a in problem.get().lower() for a in add_text):
        for i in numbers:
            addsub+=int(i)
        lb.delete(0,END)
        lb.insert(END, addsub)
    elif any(a in problem.get().lower() for a in sub_text):
        addsub=int(numbers[0])-int(numbers[1])
        lb.delete(0, END)
        lb.insert(END, addsub)
    else:
        lb.delete(0, END)
        lb.insert(END, "I don't understand")
    e1.delete(0,END)

win=Tk()
win.geometry('500x400')
win.configure(bg='lightskyblue')

l1=Label(win, text="Smart Calculator", width=20, padx=3)
l1.place(x=190, y=10)

l2=Label(win, text="I am another field of questionable need")
l2.place(x=150, y=40)

l3=Label(win, text="How can i help you")
l3.place(x=200, y=130)

problem=StringVar()
e1=Entry(win, textvariable=problem)
e1.place(x=190, y=160)


b1=Button(win, text="Help me with this", command=operation)
b1.place(x=200,y=200)

lb=Listbox(win)
lb.place(x=190,y=230)


win.mainloop()