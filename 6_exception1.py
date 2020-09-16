def ask_user():
    questions = {'qst': 'how are you?', 'ans': 'Good!', 'qst1': 'what are you doing?', 'ans1': 'I\'m slepping!'}

    while True:
        try:
            say = input('input your questions:')
            if say.lower() == questions['qst']:
                print(questions['ans'])
            elif say.lower() == questions['qst1']:
                print(questions['ans1'])
            else:
                print('I don\'t understand')

        except KeyboardInterrupt:
            print('\nBye!Bye!')
            break


if __name__ == "__main__":
    ask_user()
