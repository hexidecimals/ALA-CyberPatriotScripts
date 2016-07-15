import tkinter
from tkinter import *

# Callback func_ defined
def unlock():
        uinput_=txt.get()
        if uinput_ == "password":
                window.configure(background='#00ff00')
                lbl.configure(text='Logged in.',bg='#00ff00')
                
        else:
                window.configure(background='#ff0000')
                lbl.configure(text='Log in Failed\nTry again..',bg='#ff0000')
      


    # Makes a window
window = tkinter.Tk()

    # Title of the window
window.title('Tkinter Example #1')

    # size of the window
window.geometry('200x150')

    # Background of the window
window.configure(background='#aaaaaa')


    # Icon in top-right corner BUG?
    # window.wm_iconbitmap('Dragon.ico')



    # Makes a label called 'lbl'.
lbl = tkinter.Label(window, text= 'What\'s the password?', bg='#aaaaaa')

    # Makes a text entry called 'txt'
txt = tkinter.Entry(window,show='*')



    # Makes a button caled 'btn'
btn = tkinter.Button(window, text='Login',highlightcolor= '#ffffff', activebackground='#ffffff',background='#bbbbbf', command= unlock)
button2= tkinter.Button(window,fg='#000000',bg='#bbbbbf',text='Exit',command= exit) 


    # pack EVERYTHING!!!
lbl.pack()
txt.pack()
btn.pack()
button2.pack()




    # This is used to start the window
window.mainloop()





