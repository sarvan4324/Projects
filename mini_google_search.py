from tkinter import *
import datetime
import pyjokes
import webbrowser as wb
import speech_recognition as sr
import pyttsx3 as pt
from PIL import Image,ImageTk
import pyaudio
import requests
from bs4 import BeautifulSoup
import pywhatkit


root=Tk()
str=StringVar()
def takedata(event):
    global str
    data1=str.get()
    

    try: 

     if "play" in data1:
         data1=data1.replace("play","")
         pywhatkit.playonyt(data1)
     elif "open" in data1:
        wb.open_new("https://www.youtube.com") 
     else:
       url="https://www.google.com/search?q="+ data1
       wb.open_new(url)
    except sr.UnknownValueError:
            print("could not make out ")    
 


def speak():
    l1=Label(root,text="Listening....",font=("helvetica",70,"bold"))
    l1.place(x=600,y=750)
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            l1.destroy()
            l2=Label(root,text="recognizing.....",font=("helvetica",70,"bold"))
            l2.place(x=600,y=750)
            data=recognizer.recognize_google(audio)
            l2.destroy()





            if "play" in data:
                data=data.replace("play","")
                pywhatkit.playonyt(data)
            elif "open" in data:
                wb.open_new("https://www.youtube.com") 
            else:
               url="https://www.google.com/search?q="+ data
               wb.open_new(url)
            
        except sr.UnknownValueError:
            print("could not make out ")   
            l2.destroy()
 



img1=Image.open("mini_google_wallpaper.jpg")
img1=img1.resize((2000,1300),Image.ANTIALIAS)
photo1=ImageTk.PhotoImage(img1)
w1=Label(root,image=photo1)
w1.place(x=0,y=0)



w2=Label(root,text="mini Google search",font=("helvetica",50,"bold"),bg="grey")
w2.place(x=580,y=280)

w3=Entry(root,textvariable=str,width=70,font=("helvetica",13,"bold"))
w3.place(x=390,y=650,width=850,height=40)

img2=Image.open("mic.jpg")
img2=img2.resize((80,36),Image.ANTIALIAS)
photo2=ImageTk.PhotoImage(img2)

w4=Button(root,image=photo2,command=speak,width=80)
w4.place(x=1220,y=650)

root.bind("<Return>",takedata)


root.mainloop()