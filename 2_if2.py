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

def compare_strings(string1, string2):
  if string1 != str(string1) or string2 != str(string2):
    return 0
  else:
    if string1 == string2:
      return 1
    else:
      if len(string1) > len(string2):
        return 2
      elif string2 == "learn":
        return 3


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    first = compare_strings(5, 5)
    print(first)
    second = compare_strings('3', 5)
    print(second)
    third = compare_strings(5, '3')
    print(third)
    fourth = compare_strings('5', '5')
    print(fourth)
    fifth = compare_strings('3', '5')
    print(fifth)
    sixth = compare_strings('hey', 'hey')
    print(sixth)
    seventh = compare_strings('hey', 'learn')
    print(seventh)
    eighth = compare_strings('learn', 'hey')
    print(eighth)
if __name__ == "__main__":
    main()
