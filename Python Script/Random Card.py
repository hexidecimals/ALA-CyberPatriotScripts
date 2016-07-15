import random
import tkinter

n=4
x=0

List=["Diamonds","Hearts","Clubs","Spades"]


def Draw():
    x=random.randint(1,13)
    y=random.randint(0,3)
    if x==11:
        lbl.configure(text="Jack of "+List[y])
        print("Jack of "+List[y])
    elif x==12:
        lbl.configure(text="Queen of "+List[y])
        print("Queen of "+List[y])
    elif x==13:
        lbl.configure(text="King of "+List[y])
        print("King of "+List[y])
    elif x==1:
        lbl.configure(text="Ace of "+List[y])
        print("Ace of "+List[y])
    else:
        lbl.configure(text=str (x)+" of "+List[y])
        print(str (x)+" of "+List[y])

    
window = tkinter.Tk()
window.title('Pick a card...')
window.geometry('150x100')
window.configure(bg='#bbbbbf')

btn = tkinter.Button(window, text='Draw',highlightcolor= '#bbbbbf', activebackground='#bbbbbf',background='#bbbbbf', command= Draw)
lbl = tkinter.Label(window, bg='#bbbbbf')


lbl.pack()
btn.pack(fill = tkinter.X)

window.mainloop()
exit()
