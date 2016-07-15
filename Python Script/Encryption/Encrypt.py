import tkinter

ListO=['#',"q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","m",'m',"k","l","z","x","c","v","b","n","m","Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"," ","!","@",'$','%','^','&','*','(',')','-','_','=','+','~','`','/','\\','|',':','?','<','>',',','.','/','[',']','{','}','1','2','3','4','5','6','7','8','9','0','\'','\n','h','j']
ListX=['#',"q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","m",'m',"k","l","z","x","c","v","b","n","m","Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"," ","!","@",'$','%','^','&','*','(',')','-','_','=','+','~','`','/','\\','|',':','?','<','>',',','.','/','[',']','{','}','1','2','3','4','5','6','7','8','9','0','\'','\n','h','j']


ListX.reverse()

def Run():
    file1 = txt.get()
    file=open((file1), "r")
    text = file.read()
    file.close()

    file=open("EncryptedFile.txt","w")
    for char in text:
        file.write(ListO[int (ListX.index(char))])
    file.close()

    file=open("EncryptedFile.txt","w")
    for char in text:
        file.write(ListO[int (ListX.index(char))])
    file.close()

def Unrun():
    file1= txt.get()
    file=open((file1), "r")
    text = file.read()
    file.close()


    file=open('Decrypted.txt',"w")
    for char in text:
        file.write(ListX[int (ListO.index(char))])
    file.close()


window = tkinter.Tk()
window.title('Encryption')
window.geometry('300x150')
window.configure(bg='#aaaaaa')

lbl = tkinter.Label(window, text='What file do you want to encrypt or decrypt?',bg='#aaaaaa')
txt = tkinter.Entry(window)
btn1 = tkinter.Button(window,text= 'Encrypt',bg='#aaaaaa',command = Run)

btnDe = tkinter.Button(window,text= 'Decrypt',bg='#aaaaaa',command= Unrun)

btnE =tkinter.Button(window,text='Exit',bg='#aaaaaa',command = exit)



lbl.pack()
txt.pack()
btn1.pack(fill=tkinter.X)
btnDe.pack(fill=tkinter.X)
btnE.pack(fill=tkinter.X)

window.mainloop()

