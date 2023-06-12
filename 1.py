""" Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств """

def ListCreation(length):
    list = []
    for i in range(length):
        list.append(int(input('Input value: ')))
    print(list)
    return list

firstListLength = int(input('Input first list length: '))
secondListLength = int(input('Input second list length: '))

list1 = ListCreation(firstListLength)
list2 = ListCreation(secondListLength)

finalList = []

for i in range(firstListLength):
    for j in range(secondListLength):
        if list1[i] == list2[j]:
            finalList.append(list1[i])

 
print(finalList)