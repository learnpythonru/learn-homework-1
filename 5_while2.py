questions_and_answers: dict = {
  'как дела?': 'Хорошо!',
  'что делаешь?': 'Программирую',
  'как погода?': 'Теплеет',
  'что почитать?': 'Документацию по Python',
}


def ask_user(answers_dict: dict) -> str:

    while True:

        inp: str = input('Привет! Введите ваш вопрос: ').strip().lower()

        if inp in questions_and_answers.keys():
            print(questions_and_answers.get(inp))
        else:
            print('Не понял вопроса...')


if __name__ == "__main__":
    ask_user(questions_and_answers)
