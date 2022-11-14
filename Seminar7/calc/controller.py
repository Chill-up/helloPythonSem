import view as v
import operations as op
import log

def Button_click():
    value_a = v.GetValue() # Получаем данные с клавиатуры из view
    operationName = v.GetOperationName() #получаем оператор с клавиатуры из view * - / и т.п.
    value_b = v.GetValue()
    result = op.Operation(value_a, value_b, operationName) # запускаем вычисления из модуля функций
    v.View(result, operationName, value_a, value_b) # выводим результат во View
    log.Log(result, operationName, value_a, value_b)

