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

def main():
    def two_string_compare(str_1, str_2):
        """
        The f(x) compares 2 strings and prints out the comparison for our conditions.
        Also it returns integer results that can be stored as a variable.
        """
        msg = f"String 1: {str_1}. String 2: {str_2}. "
        if type(str_1) != str or type(str_2) != str:
            res = 0
        elif str_1 == str_2:
            res = 1
        elif len(str_1) > len(str_2):
            res = 2
        elif str_2 == "learn":
            res = 3
        else:
            res = None
        msg += f'Return: {res}'
        print(msg)
        return res

    list_1 = ['dog', 'cat', 'bag', 'learn', 1, {}, [], {"hey": "hello"}, "LOL"]
    list_2 = ['mog', 'learnlinearalgebra', 'bag', 'LOL', 'rofl', 1, 'dog', {'richard': 'rodger'}, 'learn', 'a']
    for s1 in list_1:
        for s2 in list_2:
            two_string_compare(s1, s2)

if __name__ == "__main__":
    main()
