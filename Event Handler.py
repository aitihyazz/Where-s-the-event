from tkinter import *
window=Tk()
window.geometry("100x100")
window.title("ENte handler")
def hkey(event):
    print(event.char)
window.bind("<Key>",hkey)
def hc(event):
    print("\nButton was clicked!")
button=Button(text='CLick me')
button.pack()
button.bind('<Button-1>',hc)
window.mainloop()

