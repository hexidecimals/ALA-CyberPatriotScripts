#-----------------------------------------------------
# Python 'Evolution of Text' Program
# More programs at: usingpython.com/programs
#-----------------------------------------------------

import string
import random
import time

possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' -_.,!?;:|\'\"/@#$%^&*(){}][><\\'

target = input("Enter your target text: ")
first = ''.join(random.choice(possibleCharacters) for i in range(len(target)))
second = ''

completed = False

generation = 0

while completed == False:
    print(first)
    
    second = ''
    completed = True
    for i in range(len(target)):
        if first[i] != target[i]:
            completed = False
            second += random.choice(possibleCharacters)
        else:
            second += target[i]
    generation += 1
    first = second
    time.sleep(0.1)

for i in range(10):
    print (first)
print("Target matched! That took " + str(generation) + " generation(s)")
input()
exit()
