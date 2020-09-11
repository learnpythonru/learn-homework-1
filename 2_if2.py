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
    def two_strings(string1, string2):
      if isinstance(string1, str) != True or isinstance(string2, str) != True:
        return 0        
      elif string1 == string2:
        return 1
      elif len(string1) > len(string2) and string2 == 'learn':
        return '2, 3'
      elif len(string1) > len(string2):
        return 2
      elif string2 == 'learn':
        return 3
      else:
        return 'Not specified' 
    
    print(two_strings(12234, 'test'))
    print(two_strings(12234, 12))
    print(two_strings('True', True))
    print(two_strings('test', 'test'))
    print(two_strings('test-test', 'test'))
    print(two_strings('test', 'learn'))
    print(two_strings('test-test', 'learn'))
    print(two_strings('test', 'test-test'))
        
if __name__ == "__main__":
    main()
