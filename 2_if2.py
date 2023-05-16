"""

Домашнее задание №1

Условный оператор: Сравнение строк

+ Написать функцию, которая принимает на вход две строки
+ Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
+ Если строки одинаковые, вернуть 1
+ Если строки разные и первая длиннее, вернуть 2
+ Если строки разные и вторая строка 'learn', возвращает 3
+ Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

  """


def compare_two_strig(string1:str, string2:str) -> int:
    """
    Функция сравнивает строки, выводит резулттат по условию из задания
    """
    if not (isinstance(string1, str) and isinstance(string2, str)):
        return 0
    elif string1 == string2:
        return 1
    elif len(string1) > len(string2):
        return 2
    elif string2 == "learn":
        return 3


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    str1 = "spam"
    str2 = "egg"
    str3 = "learn"
    int1 = 1

    print(str1, int1, compare_two_strig(str1, int1))
    print("*" * 80)
    print(str1, str1, compare_two_strig(str1, str1))
    print("*" * 80)
    print(str1, str2, compare_two_strig(str1, str2))
    print("*" * 80)
    print(str1, str3, compare_two_strig(str1, str3))
    print("*" * 80)
    print(str3, str2, compare_two_strig(str3, str2))


if __name__ == "__main__":
    main()
