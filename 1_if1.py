age = int(input('Введите ваш возраст: '))

def main():
  if age < 7:
    return 'Вы учитесь в детском саду'
  elif age >= 7 and age < 18:
    return 'Вы учитесь в школе'
  else:
    return 'Вы учитесь в ВУЗе или работаете'

determine_the_age = main()
print(determine_the_age)

if __name__ == "__main__":
    main()

