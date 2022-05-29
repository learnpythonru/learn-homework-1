def hello_user():
    while True:
      user = input('Как дела? ')
      if user == 'Хорошо':
        print ('Круто!')
        break
      else:
        print('Почему {}?'.format(user))

    
if __name__ == "__main__":
    hello_user()
