# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

firstString = input("Введите первую строку: ")
secondString = input("Введите вторую строку: ")

counterFirst = secondString.count(firstString) 
counterSecond = firstString.count(secondString) 

print ("Кол-во входений первой строки во вторую: "+  str(counterFirst))
print ("Кол-во входений второй строки в первую: "+  str(counterSecond))
