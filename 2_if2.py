"""

Домашнее задание №2

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
def string_compare(str1, str2):
    if isinstance(str1, str) and isinstance(str2, str):
        if str1 == str2:
            return 1
        elif str1 != str2 and str2 == 'learn':
            return 3
        elif len(str1) > len(str2):
            return 2
        else:
            pass

    else:
        return 0

def main():
    print(string_compare([1,2], 'tttx'))
    print(string_compare('python', 'python'))
    print(string_compare('learn', 'learn'))
    print(string_compare('python', 'pyon'))
    print(string_compare('python', 'learn'))
    assert string_compare(10, 'learn') == 0
    assert string_compare('learn', 'learn') == 1
    assert string_compare('hello', 'hell') == 2
    assert string_compare('learn3', 'learn') == 3



    
if __name__ == "__main__":
    main()
