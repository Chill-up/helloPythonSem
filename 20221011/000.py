# Ввести с клавиатуры 2 числа (int) и вывести в консоль их НОК (наименьшее общее кратное)

# Примитивное решение:

# number1 = int(input("Введите первое число: "))
# number2 = int(input("Введите второе число: "))

# max = max(number1, number2)
# print(max)

# if max % number1 == 0 and max % number2 == 0:
#     print(f"Наименьшее общее кратное для {number1} и {number2} = {max} ")
# else:
#     for i in range(max, number1*number2+1):
#         if i % number1 == 0 and i % number2 == 0:
#             print(f"Наименьшее общее кратное для {number1} и {number2} = {i} ")
#             break

# Правильное решение

m = int(input('Введите первое число: '))
n = int(input('Введите второе число: '))

i = 1

while (min(m, n)*i) % max(m, n):
    i += 1

print(f'НОК для {m} и {n} будет {min(m,n)*i}')
