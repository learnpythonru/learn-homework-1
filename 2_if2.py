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


def main(first_line, second_line):
    if not isinstance(first_line, str) or not isinstance(second_line, str):
        return 0
    elif first_line == second_line:
        return 1
    elif len(first_line) > len(second_line):
        if "learn" == second_line:
            return 3
        else:
            return 2
    elif "learn" == second_line:
        return 3
    return "такой комбинации не существует"

  
if __name__ == "__main__":
    print(main("привет", "мир"))
    print(main("привет", "привет"))
    print(main("привет", "солнышкоооо"))
    print(main(1, "ghbdtn"))
    print(main("hfhfhрррр", "learn"))
    print(main("hfbh", 5.32))
