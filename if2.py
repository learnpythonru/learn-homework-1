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

def strcmp(first, second):
    if not isinstance(first, str) or not isinstance(second, str):
        return 0
    elif first == second:
        return 1
    else:
        if len(first) > len(second):
            result = 2
        if second == 'learn':
            result = 3
        return result

def main():
    print(strcmp(22, True))
    print(strcmp('Python', 'Python'))
    print(strcmp('Hallelujah', 'Python'))
    print(strcmp('Python', 'learn'))

if __name__ == "__main__":
    main()
