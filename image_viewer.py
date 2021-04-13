from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title('Images Practice')
root.iconbitmap('userpassword_deusuari_787.ico') #Add icon next to title

#Define, put image inside other object and then put object in grid
#Define the image object and open the image assing to the object
my_img1 = ImageTk.PhotoImage(Image.open('corgi_images/corgi1.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('corgi_images/corgi2.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('corgi_images/corgi3.jpg'))
my_image_list = [my_img1, my_img2, my_img3] #List with all images
my_label = Label(image=my_img1)
my_label.grid(row=0,column=0, columnspan=3) #Column span takes # of columnspan
status = Label(root, text="Image 1")
status.grid(row=2,column=0, columnspan=3)
#Create a event loop, when a program ends the loop ends
n=0
def forward():
    global my_label
    global n
    my_label.grid_forget() #Delete anything inside the label
    if n < len(my_image_list)-1:
        my_label = Label(image=my_image_list[n+1])
        my_label.grid(row=0,column=0, columnspan=3) #Column span takes # of columnspan
        n+=1
    else:
        my_label = Label(image=my_image_list[0])
        my_label.grid(row=0,column=0, columnspan=3) #Column span takes # of columnspan
        n=0
def backward():
    global my_label
    global n
    my_label.grid_forget() #Delete anything inside the label
    if n > -len(my_image_list)+1:
        my_label = Label(image=my_image_list[n-1])
        my_label.grid(row=0,column=0, columnspan=3) #Column span takes # of columnspan
        n-=1
    else:
        my_label = Label(image=my_image_list[0])
        my_label.grid(row=0,column=0, columnspan=3) #Column span takes # of columnspan
        n=0
mybutton0= Button(root, text="<<", padx=40, pady=20, command=backward) #root.quit quits the program
mybutton1= Button(root, text="Exit", padx=40, pady=20, command=root.quit) #root.quit quits the program
mybutton2= Button(root, text=">>", padx=40, pady=20, command=forward) #root.quit quits the program
mybutton0.grid(row=1,column=0)
mybutton1.grid(row=1,column=1)
mybutton2.grid(row=1,column=2)
root.mainloop()
