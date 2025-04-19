from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("200x200")
def msg():
    messagebox.showwarning("ALret!","Stop virus found")
button =Button(window,text='Scanning for virus',command=msg)
button.place(x=40,y=80)
window.mainloop()