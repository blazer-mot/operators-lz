input_data = open('input.txt', 'r',) # ВАЖНО!!!  не забыть создать файл; открытие файла ввода
output_data = open('output.txt', 'w',) # преобразование числа в строку при выводе и сам вывод
n = input_data.readline() # считвание задаваемого числа как строки
# задаем переменным a и b значения первых двух чисел последовательности
a = 0
b = 1
# вывод первых двух элементов последовательности 
output_data.write(str(a))
output_data.write(str(', '))
output_data.write(str(b))
output_data.write(str(', '))
# цикл для вычисления следующих элементов
for i in range(2, int(n)):
    a, b = b, a + b # переприсваивание элементов и прибавление последнего
    output_data.write(str(b))
    if i != int(n)-1: # условие для вывода запятой с пробелом
        output_data.write(str(', '))
input_data.close() # закрытие файла считывания 
output_data.close() # закрытия файла вывода