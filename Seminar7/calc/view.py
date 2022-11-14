def View(data, operationName, value_a, value_b):
    print(f"Результат {value_a} {operationName} {value_b} = {data}")

def GetValue():
    return int(input(("Введите число: ")))

def GetOperationName():
    return input("Введите оператор (+ - = * /): ")