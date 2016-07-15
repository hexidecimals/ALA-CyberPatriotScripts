import tkinter
import random


window = tkinter.Tk()
window.title('Flip a coin.')
window.geometry('200x300')
heads = 0
tails = 0

lbl = tkinter.Label(window,text= 'I like colors...')

def red():
    lbl.configure(bg='#ff0000')
    window.configure(bg='#ff0000')

def green():
    lbl.configure(bg='#00ff00')
    window.configure(bg='#00ff00')

def blue():
    lbl.configure(bg='#0000ff')
    window.configure(bg='#0000ff')

green = tkinter.Button(window,bg='#00ff00',text='green',command= green)
    
blue = tkinter.Button(window,bg='#0000ff',text='blue',command= blue)

red = tkinter.Button(window,bg='#ff0000',text='red',command= red)


lbl.pack()
green.pack(fill=tkinter.X)
blue.pack(fill=tkinter.X)
red.pack(fill=tkinter.X)
window.mainloop()
exit()

