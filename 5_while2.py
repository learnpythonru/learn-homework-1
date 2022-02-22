questions_and_answers = {'Как дела?': 'Отлично!', 'Чем занимаешься?': 'Учусь программировать!'}

def ask_user(answers_dict):
  while True:
    questions = input('Введите вопрос: ')
    if  questions == 'Как дела?':
      print(questions_and_answers['Как дела?'])
    elif questions == 'Чем занимаешься?':
      print(questions_and_answers['Чем занимаешься?'])
    else:
      print('Неверный вопрос {}'.format(questions))
      break
   
if __name__ == "__main__":
    ask_user(questions_and_answers)
