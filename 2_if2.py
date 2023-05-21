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
    elif string2 == "learn":
        return 3
    elif len(string1) > len(string2):
        return 2


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    str_6l = "_spam_"
    str_3l = "egg"
    str_Learn = "learn"
    int_1 = 1
    dict_1 = ['dict']


    #проверяем на строку
    assert compare_two_strig(str_6l, int_1) == 0
    assert compare_two_strig(int_1, dict_1) == 0
    print("*" * 80)
    # проверяем  сравнение 2-х одинаковой длинны
    assert compare_two_strig(str_6l, str_6l) == 1
    assert compare_two_strig(str_3l, str_3l) == 1 
    print("*" * 80)
    # проверяем сравнение 2-х строк разной длинны
    assert compare_two_strig(str_6l, str_3l) == 2 
    assert compare_two_strig(str_3l, str_6l) == None 
    assert compare_two_strig(str_Learn, str_3l) == 2 
    print("*" * 80)
    # Проверяем на второе сло во Learn
    assert compare_two_strig(str_3l, str_Learn) == 3 
    assert compare_two_strig(str_6l, str_Learn) == 3 
    assert compare_two_strig(str_Learn, dict_1) == 0 
    assert compare_two_strig(dict_1, str_Learn) == 0
    print("*" * 80)


if __name__ == "__main__":
    main()
