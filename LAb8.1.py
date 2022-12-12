from array import *
bar = int(input(''))
masiv = array('i', [])
for i in range(1, bar+1):
    foo = (bar/i) / int(bar/i)
    if foo == 1:
            masiv.append(i)
print(masiv)
masiv.pop(-1), masiv.pop(0)
print(masiv)