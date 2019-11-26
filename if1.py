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

def main():
    user_num = int(input())

    if user_num < 1:
        return 'You weren\'t born yet'
    elif 1 <= user_num <= 6:
        return 'You should go to kindergarten'
    elif 7 <= user_num <= 18:
        return 'You should go to school'
    elif 19 <= user_num <= 23:
        return 'You should go to college'
    elif 24 <= user_num <= 55:
        return 'You should go to work'
    else:
        return 'You should retire'

if __name__ == "__main__":
    func_cal = main()
    print(func_cal)
