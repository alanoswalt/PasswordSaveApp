from tkinter import *

root = Tk()
root.title("Simple Calculator")

global flag
#columnspan takes more than one column, this will take 3
e = Entry(root, width=35)#.grid(row=0,column=0, columnspan=4)
e.grid(row=0,column=0,columnspan=4)


def button_click(number):
    current = e.get() #Toma lo que esta adentro de e
    #print(type(current))
    e.delete(0, END) #Delete what it is already in the box
    e.insert(0, str(current)+str(number)) #insertat algo en el label

def button_add():
    global flag
    flag = 'add'
    global first_num
    f_num=float(e.get())
    first_num = f_num
    e.delete(0, END)

def button_subs():
    global flag
    flag = 'subs'
    global first_num
    f_num=float(e.get())
    first_num = f_num
    e.delete(0, END)

def button_mult():
    global flag
    flag = 'mult'
    global first_num
    f_num=float(e.get())
    first_num = f_num
    e.delete(0, END)

def button_div():
    global flag
    flag = 'div'
    global first_num
    f_num=float(e.get())
    first_num = f_num
    e.delete(0, END)

def button_clear():
    e.delete(0, END) #Delete what it is already in the box

def button_equal():
    second_num = float(e.get())
    e.delete(0, END)
    if flag=='add':
        e.insert(0, second_num+first_num)
    elif flag=='subs':
        e.insert(0, first_num-second_num)
    elif flag=='mult':
        e.insert(0, second_num*first_num)
    elif flag=='div':
        e.insert(0, first_num/second_num)

#Define Number Buttons lambda to call a function with a parameter
mybutton0= Button(root, text="0", padx=40, pady=20, command= lambda: button_click(0))
mybutton1= Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
mybutton2= Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
mybutton3= Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
mybutton4= Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
mybutton5= Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
mybutton6= Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
mybutton7= Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
mybutton8= Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
mybutton9= Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))

#Put number Buttons
mybutton7.grid(row=1,column=0)
mybutton8.grid(row=1,column=1)
mybutton9.grid(row=1,column=2)
mybutton4.grid(row=2,column=0)
mybutton5.grid(row=2,column=1)
mybutton6.grid(row=2,column=2)
mybutton1.grid(row=3,column=0)
mybutton2.grid(row=3,column=1)
mybutton3.grid(row=3,column=2)
mybutton0.grid(row=4,column=0)

#Define extra buttons
mybuttonPlus= Button(root, text="+", padx=40, pady=20, command=button_add)
mybuttonMinus= Button(root, text="-", padx=40, pady=20, command=button_subs)
mybuttonMulti= Button(root, text="x", padx=40, pady=20, command=button_mult)
mybuttonDiv= Button(root, text="/", padx=40, pady=20, command=button_div)
mybuttonClear= Button(root, text="C", padx=40, pady=20, command=button_clear)
mybuttonEqual= Button(root, text="=", padx=40, pady=20, command=button_equal)

#Put extra buttons
mybuttonClear.grid(row=4,column=1)
mybuttonEqual.grid(row=4,column=2)
mybuttonPlus.grid(row=1,column=4)
mybuttonMinus.grid(row=2,column=4)
mybuttonMulti.grid(row=3,column=4)
mybuttonDiv.grid(row=4,column=4)

root.mainloop()
