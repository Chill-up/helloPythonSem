# global num1
# global num2

num1 = 0
num2 = 0

# def Init(a,b):
#     global num1
#     global num2
#     num1 = a
#     num2 = b

def Multiply(num1, num2):
    return num1 * num2

def Div(num1, num2):
    return num1 / num2 if num2 != 0 else "Error! Деление на ноль!"

def Sum(num1, num2):
    return num1 + num2

def Sub(num1, num2):
    return num1 - num2

def Operation(value_a, value_b, operationName):
    match operationName:
        case "*": return Multiply(value_a, value_b)
        case "+": return Sum(value_a, value_b)
        case "-": return Sub(value_a, value_b)
        case "/": return Div(value_a, value_b)