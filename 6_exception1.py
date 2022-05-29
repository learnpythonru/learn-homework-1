def hello_user():
    while True:
      try:
        user = input('Как дела? ')
        if user == 'Хорошо':
          print ('Круто!')
        else:
          print('Почему {}?'.format(user))
      except KeyboardInterrupt:
        print('Пока')
        break
        
    
if __name__ == "__main__":
    hello_user()
 