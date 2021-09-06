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
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    ##Initial setup
    exit_code=0
    age_place_list = [
          {'place':'Детскому саду', 'min_age':1, 'max_age':6}
        , {'place':'Школе', 'min_age':7, 'max_age':18}
        , {'place':'ВУЗу', 'min_age':19, 'max_age':24}
        , {'place':'Работе', 'min_age':25, 'max_age':70}
    ]

    def check_age(user_age):
        user_age=float(user_age)
        if user_age <= 0:
             print('Вы ввели неверный возраст. Возраст должен быть больше 0. Попробуйте снова')
             return 0
        elif user_age >= 130:
             print('Вы должны быть мертвы')
             return 1
        elif  70 <= user_age <130:
             print('Вы на пенсии')
             return 1     
        else :
            for i in range(len(age_place_list)):
                if age_place_list[i]['min_age'] <= user_age <= age_place_list[i]['max_age']:
                    print(f"Ваш возраст {user_age} который соответсвует {age_place_list[i]['place']}")
                    return 1
   
    while exit_code != 1:
        user_age=input('Пожалуйста введите свой возраст: ')
        exit_code=check_age(user_age)

if __name__ == "__main__":
    main()
