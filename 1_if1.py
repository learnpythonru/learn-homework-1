"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь:
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
age = int(input('Введите свой возраст: '))
def where_to_go(age):
    if age < 7:
        return 'Иди в детский сад'
    elif age >= 7 and age < 18:
        return 'Иди в школу'
    elif age >= 18 and age < 23:
        return 'Иди в ВУЗ'
    else:
        return 'Иди на работу'
result = where_to_go(age)
print(result)
