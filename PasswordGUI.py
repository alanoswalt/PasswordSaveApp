from tkinter import *

root = Tk()

def myclick():
     myLabel4 = Label(root, text="Hello "+e.get())
     myLabel4.grid(row=3,column=1)

#Creating label widget
myLabel1 = Label(root, text="Hello Worl!")
myLabel2 = Label(root, text="Sup, names Alan")
myLabel3 = Label(root, text="GOW is difficult")

#Can put width on labels, change color of background and font, borderwith7
#The get function gets everything inside the label
#insert puts default text inside the text box
e = Entry(root)
e.get()
e.insert(0, "Enter yout name")
#Button can have states (Disable) and text, padx and pady to change the size of the button, command to do something
#when the button is pressed, functions are called WITOUT parentesis, fg font color bg background color
mybutton1= Button(root, text="Put your name", command=myclick)



#Push to screen
#Grids in the scree, if you put info in other columns and the preveious ones are empty tkinter igrnores it
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=0)
myLabel3.grid(row=0,column=1)
e.grid(row=2,column=1)

mybutton1.grid(row=2,column=2)


#Create a event loop, when a program ends the loop ends
root.mainloop()
