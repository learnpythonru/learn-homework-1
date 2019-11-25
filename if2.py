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
def string_compare(string_one, string_two):
    if type(string_one) != type('str') or type(string_two) != type('str'):
        return 0
    if string_one == string_two:
        return 1
    if string_one != string_two and len(string_one) > len(string_two) and string_two != 'learn': # Это чтобы он проходил дальше и проверял
        return 2
    if string_one != string_two and string_two == 'learn':
        return 3
    
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    result1 = string_compare('test', 13)
    print(result1)
    result2 = string_compare('test', 'test')
    print(result2)
    result3 = string_compare('testing', 'test')
    print(result3)
    result4 = string_compare('python', 'learn')
    print(result4)
    resutl5 = string_compare('compare', 'comapre')
    print(resutl5)
    
if __name__ == "__main__":
    main()
