
from tkinter import *
from PIL import Image,ImageTk
from pytube import YouTube
import re
root=Tk()
#def download1(num,video_qualities):
#    video_qualities[num].download()
#    l1=Label(text="download completed") 
 #   l1.pack()      


    


def download():
    global link
    youtube_class_object=YouTube(link.get())
    video_qualities=youtube_class_object.streams.all()
    f1=Frame(root)
    f1.pack()    
    vid=list(enumerate(video_qualities))
    for i,j in vid:
        print(i,j)
    #for num,quality in vid:
     #   i=0
      #  string=str(quality)
      #  pattern="res=\"\d{3,4}p\""
       # b=re.findall(pattern,string)[0]
        #Button(f1,text=b+"  i",command=download1(num,video_qualities)).pack()
       # i+=1
    video_qualities[2].download()   
    h=Label(text="downloaded successfully",font=("Time New Roman",30,"bold"))
    h.place(x=500,y=650)
    root.after(5000,lambda:h.destroy())
    


    
def reset(event): # instead of event i can use *args
    w4.delete(0,END)    

root.title("youtube_video_downloader")
root.wm_iconbitmap("youtube_icon.jpg")
root.config(background="red")

img=Image.open("youtube_icon.jpg")
img=img.resize((300,300),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(img)

w1=Label(root,text="",bg="red")
w1.pack(pady=50)
w2=Label(root,image=photo,bg="red")
w2.pack()
w3=Label(root,text="Downloader",font=("Time New Roman",40,"bold"),bg="red")
w3.pack(pady=20)

link=StringVar()
w4=Entry(textvariable=link,width=30,font=("Terminal",20,"bold"))
w4.insert(0,"paste link here")
w4.bind("<Button-1>",reset)
w4.place(x=300,y=550,width=800,height=50)
w5=Button(text="download",font=("Time New Roman",15,"bold"),command=download,padx=10)
w5.place(x=1130,y=550,height=50)


root.mainloop()