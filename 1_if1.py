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


def user_status_based_on_age(age: int) -> str:
  if age < 0:
    return "Возраст не может быть меньше 0!"
  elif age < 3:
    return "Дети до 3х лет дожны сидеть дома на маминой титьке :)"
  elif age < 6:
    return "Дети с 3х до 6ти лет учатся в детском саду"
  elif age < 18:
    return "С 6ти лет и до 18, как правило, учатся в школе"
  elif age < 23:
    return "С 18 лет и до 23 лет учатся в ВУЗе"  # 5 лет - специалитет
  else:
    return "Добро пожаловать во взрослую жизнь! Пора работать :)"


def main():
    age = int(input("Введите ваш возраст: "))
    result = user_status_based_on_age(age)
    print(result)


if __name__ == "__main__":
    main()
