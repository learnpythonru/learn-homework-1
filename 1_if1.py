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
asfsaffffffffffffffff
"""

def main():
    while True:
        user_age = int(input("Type your age, please:\n"))
        if user_age < 2:
            print("You typed incorrect age, type correct age")
            continue
        else:
            break
    if user_age < 7:
        print("You must go to kindergarten")
    elif user_age >= 7 and user_age < 18:
        print("You must go to school")
    elif user_age >= 7 and user_age < 23:
        print('You must go to university')
    else:
        print('You must go to work')
if __name__ == "__main__":
    main()
