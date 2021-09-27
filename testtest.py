import random

def revertlist(values):
    aux = []
    for i in range(len(values)):
        aux.append(values[4-i])
    return(aux)

def maxtomin(values):
    aux = 0
    for i in range(len(values)):
        for j in range(len(values)):
            if values[i]>values[j]:
                aux= values[i]
                values[j]=values[i]
                values[j]=aux
    return values

print("\33c", end="\n")

#numberslist = [13,34,54,76,87]
numberslist = []

for i in range(5):
    numberslist.append(random.randint(10,99))

print(numberslist)

print(revertlist(numberslist))

print(maxtomin(numberslist))
