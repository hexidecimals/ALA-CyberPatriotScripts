import re

file = input('Open file to read: ')
with open(file) as f:
    cont = f.read()

Email =r"([\w\s\d\._-]+)@([\w\s\d\._-]+)(\.[\w\s\d\._-]+)"

Match = re.search(Email,cont)
if Match==True:
    print(Match.group())
print(Match)
input()
exit()
