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
    user_age = int(float((input("How old are you? "))))

    def what_you_do(age):
      if age <= 0:
        return "Let's wait till this user will born"
      elif 0 < age <= 6:
        return "User is in kindergarden"
      elif 6 < age <= 16:
        return "User studies at school"
      elif 16 < age <= 21:
        return "User studies at university"
      else:
        return "User works"
      
    result = what_you_do (user_age)
    print(result)





if __name__ == "__main__":
    main()
