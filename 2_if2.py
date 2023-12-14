"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки + 
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""


string_first = input("Как дела? ")
string_second = input("Есть новогоднее настроение? ")

print(type((string_first)))
print(type((string_second)))

len_string_first = len(string_first)
len_string_second = len(string_second)

print(len_string_first)
print(len_string_second)

def main():
    count = 1
    while count <= 4:
        if type((string_first)) is not str and type((string_second)) is not str:
            print(0)
        if string_first == string_second:
            print(1)
        if string_first != string_second and len_string_first > len_string_second:
            print(2)
        if string_first != string_second and string_second == "learn":
            print(3)
        count += 1  
if __name__ == "__main__":
    main()
