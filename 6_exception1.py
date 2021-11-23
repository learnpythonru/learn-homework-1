"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
	while True:
		try:
			user_say = input('Скажи что-нибудь: ')
			if user_say.lower() == 'пока':
				print('Ну пока')
				break
			else:
				print('Сам ты {}'.format(user_say))
		except KeyboardInterrupt:
				print('Пока!')
				break


if __name__ == "__main__":
    hello_user()
