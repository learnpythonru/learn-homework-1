#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

def check_age(age:int) -> str:
  if age < 5:
    return "you should to be in kindergarten"
  elif 5 <= age <= 17:
    return "you should to be in school"
  elif 17<= age <= 23:
    return "you should to be in Univercity"
  else:
    return "you should work"

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    age = input("Please enter yours age: ")
    result = check_age(int(age))
    print (result)

if __name__ == "__main__":
    main()
