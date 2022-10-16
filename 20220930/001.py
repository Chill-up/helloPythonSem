# Напишите программу, которая определяет позицию второго вхождения строки в списке, либо сообщит, что ее нет
#
# Пример
#
# ["qwe", "khjdhgk", "sldfs", "ertqwe", "ksdjhfqwe"] ответ 3.

list = ["qwe", "khjdhgk", "qwe", "sldfs", "ertqwe", "ksdjhfqew"]
str = input("Введите строку для поиска: ")
listOfIndex = []

for i in range(len(list)):
    if list[i] == str:
        listOfIndex.append(i)

if len(listOfIndex) > 1:
    print(f"Второе вхождение строки {str} на позици {listOfIndex[1]}")
else:
    print(f"Второго вхождения нет")
