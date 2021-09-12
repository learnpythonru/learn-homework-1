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

# возраст берется из ввода пользователя +
# user_age = input('How old are you?')

# asking user in separate function
def ask_user_age():
  user_age = None

  while not isinstance(user_age, int) or user_age >= 122 or user_age <= 0:
    try: 
      user_age = int(input('Please enter valid value between 0 and 122. How old are you? '))
    except ValueError:
      print('Is is not a number')
  
  return user_age

# верно заданя ветвления условного оператора +
# и подобраны ответы + 
def main():
  
  # не конвертируется в int
  # try: 
  #   int(user_age)
  # except ValueError:
  #   print('It is not a number')
  #   user_age = input('How old are you?')
  # else: 
  #   print('It is not a number')
  #   user_age = int(input('How old are you?'))
  
  # run until user_age won't be an int
  # can we run it until user_age won't be 
  # an int within a specific range of numbers
  
  user_age = ask_user_age()
    
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
  else:
    print('Invalid argument, please type a number within 0 - 122 range ')

# why do we see "None" after the function output? 
if __name__ == "__main__":
  main()
