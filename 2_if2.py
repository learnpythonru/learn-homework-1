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

def check_strings(str_1: str, str_2: str) -> str:
    # Check that our arguments are strings
    if isinstance(str_1, str) and isinstance(str_2, str):
        # Check that strings are equal
        if str_1 == str_2:
            return 1
        # Check that 2nd string is 'learn'
        elif str_2 == 'learn':
            return 3
        # Check that 1st string longer than 2nd
        elif len(str_1) > len(str_2):
            return 2
    else:
        return 0

def main():
    print(check_strings(123, 'gt'))   # 0
    print(check_strings('ab', 'ab'))    # 1
    print(check_strings('abc', 'ab'))   # 2
    print(check_strings('ab', 'learn')) # 3
    print(check_strings('ed', 'tgrf'))  # None
    print(check_strings('fkoo', 'ijdi'))# None
    
if __name__ == "__main__":
    main()
