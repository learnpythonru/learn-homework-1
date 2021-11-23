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
def labor_by_age(age):

  if age <= 6:
    return "Детский сад"
  elif 7 <= age <= 18:
    return "Школа"
  elif 18 <= age <= 25:
    return "ВУЗ"
  else:
    return "Работа"

def main():
    
    age = int(input("Сколько вам лет?\n"))
    labor = labor_by_age(age)
    print(labor)
    
if __name__ == "__main__":
    main()
