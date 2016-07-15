def factor(a):
    b=2
    while (int (b))<=int (a):
        while int (a)%int (b)==0:
            print(int (b))
            a=int (a)/int (b)
        if int (b)==2:
            b=3
        else:
            b=int (b)+2
a=input()
factor(int (a))
a=input()
factor(int (a))
a=input()
factor(int (a))
