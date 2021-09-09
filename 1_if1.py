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

# according to wikipedia - the oldest man 
# ever lived on earth was 122 years old
# when he died - so I took it
# as a boundary value

user_age = input('How old are you?')

def main(user_age):
  # this works only one time
  # if user enter not valid arguments secong time 
  # it falls anyway
  try: 
    int(user_age)
  except ValueError:
    print('It is not a number')
    user_age = input('How old are you?')
  else: 
    print('It is not a number')
    user_age = input('How old are you?')
    
  if 0 <= user_age <= 2:
      print(f'You are {user_age} years old')
      print('Oh, you such a baby')
  elif 3 <= user_age <= 6:
    print(f'You are {user_age} years old')
    print('You must be visiting kindergarden')
  elif 7 <= user_age <= 18:
    print(f'You are {user_age} years old')
    print('You are a pupil')
  elif 19 <= user_age <= 23:
    print(f'You are {user_age} years old')
    print('You are a college student')
  elif 24 <= user_age <= 65:
    print(f'You are {user_age} years old')
    print('You must be working')
  elif 66 <= user_age <= 122:
    print(f'You are {user_age} years old')
    print('You must be retired')
  elif not user_age:
    print('Invalid argument, please type a number within 0 - 122 range')
  else: 
    print('Invalid argument, please type a number within 0 - 122 range')

if __name__ == "__main__":
  print(main(user_age))
