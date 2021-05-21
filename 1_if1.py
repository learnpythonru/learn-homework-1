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

def definition_occupation():

    age = int(input("How old are you? \n"))
    if age <= 0:
        conclusion = "You have not yet been born."
    elif age > 0 and age < 3:
        conclusion = "You are too young to go to kindergarten. You are still with your parents."
    elif age >= 3 and age < 7:
        conclusion = "You are a student of a kindergarten."
    elif age >=7 and age < 17:
        conclusion = "You are a school student."
    elif age >=17 and age < 22:
        conclusion = "You are a student."
    elif age >=22 and age < 60:
        conclusion = "You work somewhere."
    else:
        conclusion = "You are a retiree"
    return conclusion


if __name__ == "__main__":
    print(definition_occupation())
    
