from tkinter import *
from textblob import TextBlob

def check_spelling():
    a = TextBlob(spell_check.get())
    spell = Label(window,text="the correct spelling is : ",font=("Arial",30,"bold"),bg="gray")
    spell.pack()
    
window = Tk()
window.title("my Spelling Checker")
window.geometry("800x600")
window.config(background="pink")

text_heading = Label(window,text="Spelling Checker",font=("Arial",50,"bold"),bg="black",fg="light green")
text_heading.pack()

text_check = Label(window, text="Enter the spelling",font=("arial",35,"bold"),bg="yellow",fg="red")
text_check.pack()

spell_check = Entry (window,font=("arial",45,"bold"),width=500,bg="light blue")
spell_check.pack()

check_button = Button(window, text="check!!",font=("Arial",30,"bold"),fg="white",bg="red")
check_button.pack()

window.mainloop()


