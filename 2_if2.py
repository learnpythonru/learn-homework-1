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
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    def check_strings(string_1, string_2):
        if type(string_1) != str or type(string_2) != str:
            return 0
        elif string_1 == string_2:
            return 1
        elif (len(string_1) > len(string_2)) and string_2 != "learn":
            return 2
        elif string_2 == "learn":
            return 3

    print(check_strings(42, "bebebe"))
    print(check_strings("bebebe", "bebebe"))
    print(check_strings("baububupi", "bebebe"))
    print(check_strings("bububu", "learn"))

if __name__ == "__main__":
    main()
