''' Задание 1. Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно
предыдущего. Требуется определить номер дня,на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.'''

a = int(input("Введите результат спортсмена в первый день пробежки (км): "))
b = int(input("Введите результат, к которому стремится спортсмен, увеличивая нагрузку (км): "))
day = 1
while a < b:
    a *= 1.1
    day += 1
print(f"На {day}й день результат спортсмена составит не менее {b}км!")