# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

number = input("Введите число N: ")

list = ["kjhgkd3","lkfdsjlk","weifjwh43","38955798sdfh3"]

listOfIndex = []

for i in range(len(list)):
    if list[i].find(number) != -1:
        listOfIndex.append(i)

if len(listOfIndex) > 0:
    print(f"Элементы списка с индексами {listOfIndex} содержат число {number}")
else:
    print(f"Элементы списка не содержат число {number}")