from tkinter import *
from random import *

def do_event(event):
    print("{},{}".format(event.x,event.y))

def jump(event):
    app.hello_b.place(relx=random(),rely=random())

class App:
    def __init__(self,master):
        frame = Frame(master)
        master.geometry("350x350")
        master.title("Catch me if you can!")
        master.bind("<Button-1>",do_event)
        master.bind("<Button-1>",do_event)
        frame.pack()

        self.hello_b = Button(master,text=""":P""")
        self.hello_b.bind("<Enter>",jump)
        self.hello_b.pack()




root = Tk()

app = App(root)

root.mainloop()
