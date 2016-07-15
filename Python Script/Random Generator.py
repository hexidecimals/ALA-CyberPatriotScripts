import random

n=input(
    "How many objects? "
    )

x=0

List=[]
def ListOne(n):
    x=0
    while int (x)<int (n):
        y=input("Object ")
        List.append(y)
        x+=1


ListOne(n)



g=1
a=input(
    "How many Gen?"
    )
while g<=int (a):
    y=random.randint(0,int (n)-1)
    print(List[y])
    g+=1

f=input("Exit Program...")
exit()
    
