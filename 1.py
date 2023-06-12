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