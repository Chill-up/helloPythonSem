# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

#     Примеры:

#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите 2 число: "))
# num3 = int(input("Введите 3 число: "))
# num4 = int(input("Введите 4 число: "))
# num5 = int(input("Введите 5 число: "))
# max = num1

lst = []
for i in range(0, 5):
    lst.append(int(input("Введите число: ")))

print(lst)

max = lst[0]
for i in lst:
    if i > max:
        max = i
print(max)
