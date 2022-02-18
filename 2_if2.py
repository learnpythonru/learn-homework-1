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


    def strings_comparing(st1, st2):
        if not isinstance(st1, str) or not isinstance(st2, str):
            return 0
        if st1 == st2:
            return 1
        if len(st1) > len(st2):
            return 2
        if st2 == 'learn':
            return 3
    
    print(strings_comparing(135, 654))                      # 0
    print(strings_comparing(135, "dfg"))                    # 0    
    print(strings_comparing("ressa", 345))                  # 0
    print(strings_comparing("some text", "some text"))      # 1
    print(strings_comparing("larger text", "short"))        # 2
    print(strings_comparing("short", "large text"))         # None
    print(strings_comparing("another large text", "learn")) # 2
    print(strings_comparing("sh", "learn"))                 # 3
    print(strings_comparing("learn", "not learn"))          # None


if __name__ == "__main__":
    main()
