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


def main(strings_1, strings_2):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    responded = []
    if type(strings_1) != str or type(strings_2) != str:
        responded.append("0")
    if strings_1 == strings_2:
        responded.append("1")
    elif len(str(strings_1)) > len(str(strings_2)):
        responded.append("2")
    if strings_1 != strings_2 and strings_2 == "learn":
        responded.append("3")
    if "0" in responded or "1" in responded or "2" in responded or "3" in responded:
        print(
            f'Ты ввел {strings_1} и {strings_2}, поэтому получил {", ".join(responded)}')
    else:
        print(
            f'Ты ввел {strings_1} и {strings_2}, которые не соответствуют ни одному из условий, поэтому ничего не получил')


if __name__ == "__main__":
    main(2, "learn")
    main("python", "learn")
    main("learn", "learn")
    main(2, 2)
    main("xo-xo", "learn")
    main("love", "python")
