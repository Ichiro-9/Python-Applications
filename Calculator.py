from tkinter import *
window = Tk()
#window.config(bg='#808080')
window.title('Wave Calculator🖥️')
e = Entry(window,width=47,borderwidth=4)#fg='white',bg='grey')
e.grid(row=0,column=0,columnspan=4,pady=10,padx=10)
inpu=[]
sumi=[];operation=''

def delete():
    current=e.get()
    e.delete(len(current)-1,len(current))

def button_click(number):
    e.insert(len(e.get()),number)

def button_clear():
    e.delete(0,END)

def multip():
    global operation,n1
    operation='multiply'
    n1=e.get()
    n1=float(n1)
    e.delete(0,END)

def modul():
    global operation,n1
    operation='modulo'
    n1=e.get()
    n1=float(n1)
    e.delete(0,END)

def divid():
    global operation,n1
    operation='divide'
    n1=e.get()
    n1=float(n1)
    e.delete(0,END)

def subtrac():
    global operation,n1
    operation='subtract'
    n1=e.get()
    n1=float(n1)
    e.delete(0,END)

def square1():
    n1=e.get()
    n1=float(n1)
    e.delete(0,END)
    if str(n1**2)[-2:]=='.0':
        e.insert(0,str(n1**2)[:-2])
    else:

        e.insert(0, str(n1 ** 2))

def p1():
    e.delete(0, END)
    e.insert(0,22/7)

def cube1():
    global operation,n1
    operation='exponent'
    n1=e.get()
    n1=float(n1)
    e.delete(0,END)


def input_add():
    global operation,n1
    operation='add'
    n1=e.get()
    n1=float(n1)
    e.delete(0,END)

def by():
    n1=e.get()
    e.delete(0,END)
    e.insert(0,1/int(n1))
def equal1():
    global operation
    if operation=='add':
        per=float(e.get())
        e.delete(0, END)
        if str(n1+per)[-2:] == '.0':
            e.insert(0, str(n1+per).split('.')[0])
        else:
            e.insert(0, str(n1+per))
        operation=None
    if operation=='subtract':
        per=float(e.get())
        e.delete(0, END)
        if str(n1-per)[-2:] == '.0':
            e.insert(0, str(n1-per).split('.')[0])
        else:
            e.insert(0, str(n1-per))
        operation=None
    if operation=='multiply':
        per=float(e.get())
        e.delete(0, END)
        if str(n1*per)[-2:] == '.0':
            e.insert(0, str(n1*per).split('.')[0])
        else:
            e.insert(0, str(n1*per))
        operation=None
    if operation=='divide':
        per=float(e.get())
        e.delete(0, END)
        if str(n1/per)[-2:] == '.0':
            e.insert(0, int(n1//per))
        else:
            e.insert(0, str(n1/per))
        operation=None
    if operation=='modulo':
        per=float(e.get())
        e.delete(0, END)
        e.insert(0, int(n1%per))

        operation=None
    if operation == 'exponent':
        pre = float(e.get())
        e.delete(0, END)
        if str(n1 ** pre)[-2:] == '.0':
            e.insert(0, str(n1 ** pre)[:-2])
        else:
            e.insert(0, str(n1 ** pre))
        operation=None
     
button1=Button(window,text='1',padx=30,pady=15,command=lambda: button_click(1))
button2=Button(window,text='2',padx=30,pady=15,command=lambda: button_click(2))
button3=Button(window,text='3',padx=30,pady=15,command=lambda: button_click(3))
button4=Button(window,text='4',padx=30,pady=15,command=lambda: button_click(4))
button5=Button(window,text='5',padx=30,pady=15,command=lambda: button_click(5))
button6=Button(window,text='6',padx=30,pady=15,command=lambda: button_click(6))
button7=Button(window,text='7',padx=30,pady=15,command=lambda: button_click(7))
button8=Button(window,text='8',padx=30,pady=15,command=lambda: button_click(8))
button9=Button(window,text='9',padx=30,pady=15,command=lambda: button_click(9))
button0=Button(window,text='0',padx=30,pady=15,command=lambda: button_click(0))




#creating additional ones
decimal=Button(window,text=".",padx=30,pady=15,command=lambda: button_click('.'))
add= Button(window,text="+",padx=30,pady=15,command=lambda: input_add())
subtract = Button(window,text='-',padx=30,pady=15,command= lambda: subtrac())
multiply=Button(window,text='×',padx=30,pady=15,command=lambda: multip())
divide=Button(window,text='÷',padx=30,pady=15,command=lambda: divid())
equal = Button(window,text="=",padx=30,pady=15,command=lambda: equal1())
clear= Button(window,text="Clear",padx=60,pady=15,command=lambda: button_clear())
backspace=Button(window,text='del',padx=30,pady=15,command=lambda :delete())
modulo=Button(window,text='%',padx=30,pady=15,command=lambda : modul())
sqaure=Button(window,text='x²',padx=30,pady=15,command=lambda : square1())
exponent=Button(window,text='xⁿ',padx=30,pady=15,command=lambda : cube1())
pi=Button(window,text='¶(PI)',padx=24,pady=15,command=lambda : p1())
by1 = Button(window,text='⅟',padx=30,pady=15,command=lambda : by())


#placing them
button9.grid(row=2,column=0)
button8.grid(row=2,column=1)
button7.grid(row=2,column=2)
button6.grid(row=3,column=0)
button5.grid(row=3,column=1)
button4.grid(row=3,column=2)
button3.grid(row=4,column=0)
button2.grid(row=4,column=1)
button1.grid(row=4,column=2)
button0.grid(row=5,column=1)
decimal.grid(row=5,column=0)
add.grid(row=5,column=3)
subtract.grid(row=4,column=3)
multiply.grid(row=3,column=3)
divide.grid(row=2,column=3)
equal.grid(row=5,column=2)
clear.grid(row=1,column=0,columnspan=2)
backspace.grid(row=1,column=3)
modulo.grid(row=1,column=2)
sqaure.grid(row=6,column=0)
exponent.grid(row=6,column=1)
pi.grid(row=6,column=2)
by1.grid(row=6,column=3)

window.mainloop()