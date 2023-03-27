from phonenumbers import carrier,geocoder,timezone
import phonenumbers
from tkinter import *
from PIL import Image,ImageTk


def details():

 phone=phonenumbers.parse(str.get())
 time=timezone.time_zones_for_number(phone)
 carr=carrier.name_for_number(phone,"en")
 reg=geocoder.description_for_number(phone,"en")




 f2=Frame(root)
 f2.place(x=1000,y=500)

 img1=Image.open("hack.jpg")
 img1=img1.resize((500,300))
 photo1=ImageTk.PhotoImage(img1)
 w10=Label(f2,image=photo1)
 w10.place(x=0,y=0)

 w6=Label(f2,text=f"Time Zone: {time}",font=("helvetica",20,"bold"))
 w6.pack(anchor="w",pady=10)
 w7=Label(f2,text=f"Type of SIM: {carr}",font=("helvetica",20,"bold"))
 w7.pack(anchor="w",pady=10)
 w8=Label(f2,text=f"Registration: {reg}",font=("helvetica",20,"bold"))
 w8.pack(anchor="w",pady=10)
 root.after(10000,lambda:f2.destroy())


def reset(event):
    w3.delete(0,END)
root=Tk()

img2=Image.open("wallpaper.jpg")
photo=ImageTk.PhotoImage(img2)

str=StringVar()
str.set("type here")
w1=Label(root,image=photo)
w1.place(x=0,y=0)
w5=Label(root,text="Enter phone number:",font=("Arial",20,"bold"))
w5.place(x=105,y=250)
w2=Label(root,text="Phone Number Details",font=(" Time New Roman",40,"bold"),fg="white",bg="black")
w2.pack(pady=50)
f1=Frame(root)
f1.place(x=100,y=300)
w3=Entry(f1,textvariable=str,width=15,font=("System",30,"bold"))
w3.pack(side=LEFT)
w3.bind("<Button-1>",reset)

img=Image.open("fetch.jpg")
img=img.resize((140,140))
click=ImageTk.PhotoImage(img)

w4=Button(root,image=click,command=details,borderwidth=10,bg="grey")
w4.place(x=590,y=265)




root.mainloop()