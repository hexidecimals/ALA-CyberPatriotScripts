def count_char(text,char):
    count = 0
    for c in text:
        if c== char:
            count +=1
    return count

filename = input("Name of file::")
with open(filename) as f:
    text = f.read()


for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()|\-=_+;:'?/>.<,`~":
    perc = count_char(text,char)
    if not perc==0:
        print("{0} x {1}".format(char,round(perc,2)))

print(input())
