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
#DONE

def str_comparing(str1, str2):
    if (type(str1)!=str) and (type(str2)!=str) :
        return 0
    if str1 == str2:
        return 1
    elif str1 !='Learn' and  str2 == 'Learn':
        return 3
    elif len(str1) > len(str2):
        return 2



print(str_comparing(5, 10))
print(str_comparing("Two str is the same", "Two str is the same"))
print(str_comparing("Loooooong", "Short"))
print(str_comparing("Some random", "Learn"))
    
