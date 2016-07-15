# Changes a text file to become unreadable

inputx = input('Render what (txt only) file?: ')

file=open(inputx, "r")
text = file.read()
file.close()


file=open(inputx,"w")
for char in text:
    file.write(char + '<(\#/)>')
file.close()

print('To fix: \nUse replace all tool\nReplace \"<(\#/)>\" with nothing\nand it should work again...')
print("\n")
input("Exit...")
exit()




