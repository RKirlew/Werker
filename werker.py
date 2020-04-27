import praw
from tkinter import ttk
from tkinter import *
import tkinter.filedialog
from PIL import ImageTk, Image

import win32api
from time import sleep
import os
import schedule
import os.path
from os import path

bg='werker.jpg'
"""" Simple PRAW Project by Raheem"""
r = praw.Reddit(user_agent='LMGTFY (by /u/USERNAME)',
                     client_id='GETTHISYOURSELF', client_secret="GETTHISYOURSELF",
                    )
newLim=5
def file_save():
    global fName
    files=[('Text File','*.txt')]
    fName=tkinter.filedialog.asksaveasfile(filetypes=files,mode='w',defaultextension=files)
    if fName is None:
        
        return
   
def display():
    
    root=Tk()
    root.geometry("820x400+300+150")
    root.resizable(width=False,height=False)
    root.overrideredirect(1)

    img=ImageTk.PhotoImage(Image.open(bg))
    panel = Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    root.after(4500, lambda: root.destroy()) # Destroy the widget after 30 seconds
    root.focus_force()

    root.mainloop()
def startup():
    display()
    
    global txt
    global loc
    global sub
    global title
    global titleVar
    global subVar
    global limVar
    
    window=Tk()
    titleVar=tkinter.StringVar()
    subVar=tkinter.StringVar()
    limVar=tkinter.StringVar()


    window.title("Werker - A Bored Programmer's Utility")
    window.geometry('350x200+600+300')
    btn= Button(window,text="Start Werking",command=werk)
    btn.grid(column=2,row=1)
    lbl=Label(window,text="Werk Limit:")
    lbl.grid(column=0,row=0)
    txt=Entry(window,width=10,textvariable=limVar)
    txt.grid(column=1,row=0)
    lbl=Label(window,text="Subreddit (ex: python):")
    lbl.grid(column=0,row=1)
    sub=Entry(window,width=20,textvariable=subVar)
    sub.grid(column=1,row=1)
    lbl=Label(window,text="Title to search for:")
    lbl.grid(column=0,row=2)
    title=Entry(window,width=20,textvariable=titleVar)
    title.grid(column=1,row=2)
    sv=Button(window,text="Select file location",command=file_save)
    sv.grid(column=2,row=0)
    
    

    window.mainloop()
  
def werk():
    #test()
    
    """if path.exists(fName.name):
        os.remove(fName.name)"""
    if not limVar.get():
        limit=5
    else:    
        limit=int(limVar.get())
    
    tTl=titleVar.get()
    subR=subVar.get()
    if tTl=="":
        tTl="working on this week"
    if subR=="":
        subR="python"
    subm=r.subreddit(subR)
    
  
    for submission in subm.hot(limit=10):
        if tTl in submission.title:
            win32api.MessageBox(0,'Werk created!','Werker')
            werk=r.submission(id=submission.id)
        else:
            for submission in subm.new(limit=10):
                if tTl in submission.title:
                    win32api.MessageBox(0,'New werk found!','Werker')
                    werk=r.submission(id=submission.id)
           
    for toppers in werk.comments:
           
            if limit >0:
                limit-=1
                dat="\nWerk by u/"+str(toppers.author.name)+" "+str(limit)+") --> "+toppers.body+"\n"
                
                f=open(fName.name,"a",encoding='utf-8')
                f.write(dat)
    print("test")             


        
        


startup()
schedule.every().monday.do(werk)

while True:
    #test()
    schedule.run_pending()
    
    print("work")
    sleep(1)
