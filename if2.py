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
a = "string1"
b = "learn"


def main(a, b):

    if(type(a) != str) and (type(b) != str):
        return 0
    # elif a == b:
    #     return 1
    # elif len(a) > len(b) or a != b:
    #     return 2
    # elif a != b or b == 'learn':
    #     return 3
    else:
        return 404

print(main(a, b))


#     if discount >= max_discount or "iphone" in name.lower() or not name:

    
if __name__ == "__main__":
    main(a, b)
