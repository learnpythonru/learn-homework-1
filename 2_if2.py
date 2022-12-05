"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(str1, str2): 
    value1 = (isinstance(str1, str))
    value2 = (isinstance(str2, str))
    if value1 != True and value2 != True:
        return '0'
    elif str1 == str2:
        return '1'
    elif str1 != str2 and len(str1) > len(str2):
        return '2'
    elif str1 != str2 and str2 == 'python':
        return '3'


print(main(1, 2))
print(main('London', 'London'))
print(main('Winter is coming', 'Hear me roar!'))
print(main('poo', 'python'))
  
    

