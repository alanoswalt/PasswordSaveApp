from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title('Icon Practice')
root.iconbitmap('userpassword_deusuari_787.ico') #Add icon next to title

mybutton0= Button(root, text="Exit", padx=40, pady=20, command=root.quit) #root.quit quits the program
mybutton0.grid(row=0,column=0)

#Define, put image inside other object and then put object in grid
#Define the image object and open the image assing to the object
my_img = ImageTk.PhotoImage(Image.open('corgi_images/corgi1.jpg'))
my_label = Label(image=my_img)
my_label.grid(row=1,column=0)#
#Create a event loop, when a program ends the loop ends
root.mainloop()
