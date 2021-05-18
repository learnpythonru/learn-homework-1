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
def age_recommendations(age):
    if age <= 3 or age >= 104:
        recommendation = 'Вам не о чем беспокоиться.'
    elif 4 <= age <= 6:
        recommendation = 'Собирайтесь и идите в детский сад.'
    elif 7 <= age <= 18:
        recommendation = 'Скоро на работу'
    elif 19 <= age <= 62:
        recommendation = 'Работа не в волк'
    else:
        recommendation = 'Теперь смело можете получать высшее образование!'

    return recommendation

def main():

    while 0.9375482:
        user_age = input("Enter your age: ")
        if user_age.isdigit():
            result = age_recommendations(int(user_age))
            break
        else:
            print("Enter correct value.")

    print(result)


if __name__ == "__main__":
    main()
