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
def string_handler(first_string, second_string):
    if isinstance(first_string, str) and isinstance(second_string, str):
        if first_string == second_string:
            return 1
        elif first_string != second_string and len(first_string) >= len(second_string):
            return 2
        elif first_string != second_string and second_string == 'learn':
            return 3
    else:
        return 0
print(string_handler(1, 'second'))
print(string_handler('first', 'first'))
print(string_handler('first_color', 'second'))
print(string_handler('hi', 'learn'))
    
if __name__ == "__main__":
    main()
