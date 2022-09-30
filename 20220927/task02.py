# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

firstString = str(input("Введите первую строку: "))
secondString = str(input("Введите вторую строку: "))
count = 0

for i in range(len(secondString) + 1):
    substringLength = len(firstString) + i
    if firstString == secondString[i:substringLength]: #двигаемся по строке и проверяем вхождения
        count += 1
print(count)
