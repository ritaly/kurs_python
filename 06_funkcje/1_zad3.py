def sumowanie(lista):
    return sum(lista)

str_num = input("Podaj listę liczb: ")
list_num = str_num.split()

list_int = []
for i in list_num:
    list_int.append(int(i))

print(sumowanie(list_int))
