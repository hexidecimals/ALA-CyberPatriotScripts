import random

bits = '01'

File = open('RandomBinaryCode.txt','w')

def Set():
    x=0
    while x<4:
        File.write(random.choice(bits))
        x+=1
    File.write(' ')

user=input('How many sets?: ')
z=0
while z<int (user):
    Set()
    z=z+1
    if z==int (user):
        break

File.close()

print("RandomBinaryCode now has "+ user + ' Byte(s)')
input()
exit()
