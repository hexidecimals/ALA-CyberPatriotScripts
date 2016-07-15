import tkinter
import random
import time


window = tkinter.Tk()
window.title('COLORSSS!!!!.')
window.geometry('300x300')
heads = 0
tails = 0

List= ['1','2','3','4','5','6','7','8','9','a','f','b']


def master():
    change()

   
def change():
    a='#'
    b=random.choice(List)
    c=random.choice(List)
    d=random.choice(List)
    f=random.choice(List)
    g=random.choice(List)
    h=random.choice(List)
    window.configure(background=a+b+c+d+f+g+h)
    btn.configure(background=a+b+c+d+f+g+h)
    lbl.configure(background=a+b+c+d+f+g+h,text=a+b+c+d+f+g+h)





btn = tkinter.Button(window,text='Change Color',command= master)
lbl = tkinter.Label(window) 
lbl.pack()
btn.pack(fill = tkinter.X)
window.mainloop()
exit()

