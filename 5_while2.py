def ask_user_dict():
    questions = {'qst': 'how are you?', 'ans': 'good!', 'qst1': 'what are you doing?', 'ans1': 'I slepping'}

    while True:
        say = input('input your questions:')
        if say.lower() == questions['qst']:
            print(questions['ans'])
        elif say.lower() == questions['qst1']:
            print(questions['ans1'])
        else:
            print('i don\'t know')

if __name__ == "__main__":
    ask_user_dict()
