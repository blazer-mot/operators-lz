input_data = open('input.txt', 'r',) # ВАЖНО!!!  не забыть создать файл; открытие файла ввода
output_data = open('output.txt', 'w') # создание и открытие файла для вывода ответа
data = input_data.read() # считываем число
a = int(data) # переводим число в int
for i in range(2, 25001): # в цикле проверяем чтобы число делилось на 1 и само на себя
    if a % i == 0 and a != i: # условие для неверно
        output_data.write('N') # преобразование числа в строку при выводе и сам вывод
        break # прекращение выполнения цикла
    elif a == i: # условие для верно
        output_data.write('Y') # преобразование числа в строку при выводе и сам вывод
    elif a == 1: # частный случай для 1
        output_data.write('N') # преобразование числа в строку при выводе и сам вывод
input_data.close() # закрытие файла считывания 
output_data.close() # закрытия файла вывода