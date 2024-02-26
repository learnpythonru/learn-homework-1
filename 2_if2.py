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

def string_checking(str1, str2):
    if not(isinstance(str1, str) and isinstance(str2, str)):
        return 0
    if str1 == str2:
        return 1
    if str1 != str2 and str2 == 'learn':
        return 3
    elif len(str1) > len(str2):
        return 2
    else:
        return -1

def main():
    print(string_checking('italy','italy'))
    print(string_checking('denmark', 'poland'))
    print(string_checking('russia', 'learn'))
    print(string_checking(7, 'python')) 
   
   
if __name__ == "__main__":
    main()
