import random
from typing import Sized

def sort_assending():
    lista=list(range(13,33))
    print(lista)
    lista.sort()
    print(lista)
    lista.reverse()
    print(lista)

def revert_order(values):
    aux = []
    for i in range(len(values)):
        aux.append(values[len(values)-1-i])
    return aux


#this sentence clear the terminal window
print("\033c", end="")

randomlist = []

#Create a list of 7 random numbers
for i in range(7):
    randomlist.append(random.randint(10,99))
print(randomlist)

print(revert_order(randomlist))
randomlist.reverse()
print(randomlist)