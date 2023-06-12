# тут я условия задачи не совсем понял) По условию выходит что просто 3 куста на количество ягод умножить нужно, т.к. позиция изначально задана.

import random

def GryadkaPosajena(length):
    gryadka = []
    for i in range(length):
        gryadka.append(random.randint(0, 10))
    print(gryadka)
    return gryadka

def ClubnikaSearch(gryadka):
    maxYagodok = 0
    for i in range(len(gryadka)):
        if maxYagodok < gryadka[i-2] + gryadka[i-1] + gryadka[i]:
            maxYagodok = gryadka[i-2] + gryadka[i-1] + gryadka[i]
    print(maxYagodok)

gryadkaLength = int(input("Input gryadka length: "))
gryadka = GryadkaPosajena(gryadkaLength)
ClubnikaSearch(gryadka)
