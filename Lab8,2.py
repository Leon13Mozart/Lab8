import numpy as num
import random as r

N = int(input("Введіть число N: "))

num_masiv = num.zeros((N,N), dtype = num.int)
num_ryad = 0 
plural = 0

for a in range (N):
    for b in range (N):
        el = r.randint(1,12)

        if el in num_masiv:
            num_masiv [a][b] = 0
        else:
            num_masiv [a][b] = el
        if b == num_ryad:
            plural = plural + int(num_masiv [a][b])
            
    num_ryad += 1
print(num_masiv) 
print(plural)