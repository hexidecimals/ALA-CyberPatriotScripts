import tkinter
import random


window = tkinter.Tk()
window.configure(bg='#aaaaaa')
window.title('Flip a coin.')
window.geometry('200x150')
heads = 0
tails= 0
lbl = tkinter.Label(window,bg='#aaaaaa',text='Heads: '+str(heads)+' Tails: '+str(tails))
x=0
def run():
    global x
    x=txt.get()
    for i in range(int(x)):
        flip()

def flip():
    global heads
    global tails
    n=random.randint(0,1)
    if n==0:
        heads+=1
        print('Heads!')
        lbl2.configure(text='Heads!')
    else:
        tails+=1
        print('Tails!')
        lbl2.configure(text='Tails!')
    
    lbl.configure(text='Heads: '+str(heads)+' Tails: '+str(tails))


def setonce():
    x=txt.get()


txt = tkinter.Entry(window)


btn2 = tkinter.Button(window,text='Enter number of flips.',command=run,bg='#aaaaaa')

lbl2 = tkinter.Label(window,bg='#aaaaaa')

btn = tkinter.Button(window,text='Flip once.',command=flip,bg='#aaaaaa')


lbl.pack(fill=tkinter.X)
lbl2.pack(fill=tkinter.X)
txt.pack()
btn.pack(fill=tkinter.X)
btn2.pack(fill=tkinter.X)
window.mainloop()
exit()
