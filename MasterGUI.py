import subprocess
import tkinter
from tkinter import *



    # Makes a window
window = tkinter.Tk()

    # Title of the window
window.title('Master Gui')

    # size of the window
window.geometry('250x150')

    # Background of the window
window.configure(background='#aaaaaa')


def Audit():
        subprocess.run('Audit.bat')

def TakeOwn():
        subprocess.run('TakeOwn.bat')

def GodmodeOn():
        subprocess.run('GodmodeOn.bat')

def Network():
        subprocess.run('Network.bat')

def Violations():
        subprocess.run('Violations.bat')

def Batchchecker():
        subprocess.run('Batchchecker.bat')


lbl = tkinter.Label(window,text='What would you like to do?',background='#aaaaaa')

Auditbtn = tkinter.Button(window, text='Turn on Audit Policies',background='#aaaaaa', command= Audit)

Ownbtn = tkinter.Button(window, text='Take ownership of files',background='#aaaaaa', command= TakeOwn)

Modebtn = tkinter.Button(window, text='Godmode On',background='#aaaaaa', command= GodmodeOn)

Netbtn = tkinter.Button(window, text='Get Network status',background='#aaaaaa', command= Network)

Viobtn = tkinter.Button(window, text='Check for Media Files',background='#aaaaaa', command= Violations)

Batbtn = tkinter.Button(window, text='Check for batchfiles',background='#aaaaaa', command= Batchchecker)


button2= tkinter.Button(window,fg='#000000',bg='#aaaaaa',text='Exit',command= exit) 


lbl.pack()
Auditbtn.pack(fill = tkinter.X)
Ownbtn.pack(fill = tkinter.X)
Modebtn.pack(fill = tkinter.X)
Netbtn.pack(fill = tkinter.X)
Viobtn.pack(fill = tkinter.X)
Batbtn.pack(fill = tkinter.X)


button2.pack(fill = tkinter.X)




    # This is used to start the window
window.mainloop()





