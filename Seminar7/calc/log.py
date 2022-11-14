from datetime import datetime as dt

path = "log.txt"

def Log(result, operationName, value_a, value_b):
    string = f"Результат {value_a} {operationName} {value_b} = {result} | {dt.now()} \n"
    with open(path,"a", encoding="utf-8") as data:
        data.write(f'{string}\n')
