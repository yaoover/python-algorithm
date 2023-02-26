a = input("please enter anything : ")
listA = list(a)
print(listA)
for i in listA:
    if ' ' in listA:
        listA.remove(' ')

print(listA)