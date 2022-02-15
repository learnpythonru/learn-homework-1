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

def comparison(string_1, string_2):
    if type(string_1) is not str and type(string_2) is not str:
        return 0
    else:
        string_1 = str(string_1)
        string_2 = str(string_2)
    if string_1 is string_2:
        return 1
    else:
        if len(string_1) > len(string_2):
            if string_2 != "learn":
                return 2
            else:
                return 2, 3
        elif string_2 == "learn":
            return 3
                          

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    
    TEST_LIST = [(12, 12), ("word", "word"), ("world", "word"), ("world", "learn"), ("worlds", "learn")]
    
    for string_1, string_2 in TEST_LIST:
        print(comparison(string_1, string_2))

    
if __name__ == "__main__":
    main()
