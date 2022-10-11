# Ввести с клавиатуры 2 числа (int) и вывести в консоль их НОК (наименьшее общее кратное)

number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))

max = max(number1, number2)
print(max)

if max % number1 == 0 and max % number2 == 0:
    print(f"Наименьшее общее кратное для {number1} и {number2} = {max} ")
else:
    for i in range(max, number1*number2+1):
        if i % number1 == 0 and i % number2 == 0:
            print(f"Наименьшее общее кратное для {number1} и {number2} = {i} ")
            break
