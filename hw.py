# -*- coding: utf-8 -*-
"""
Created on Thu May 12 17:56:48 2022

@author: zoya sharma
"""

from tkinter import*

root=Tk()
root.title("FIBONACCI SUM")
root.geometry("400x250")
root.configure(background='light blue')

enter_word=Entry(root)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)

label=Label(root,text="name in ASCII: ",bg="light cyan",fg="black")
label2=Label(root,text="encryped name:  ",bg="light cyan",fg="black")

def ASCII():
    input_word=str(enter_word.get())
    
    for letter in input_word:
        label["text"]+=str(ord(letter))+" "
        ASCCII=int(ord(letter))
        encryped=ASCII-1
        label2["text"]+=str(chr(encryped))
        

btn=Button(root,text="display the ASCII and encryped",command=ASCII,bg="royalblue",fg="white")
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

label.place(relx=0.5,rely=0.6,anchor=CENTER)
label2.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()