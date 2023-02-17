import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def answer_incorrect(result, user_answer, name):
    print(f'\'{user_answer}\' is wrong answer ;(.', end=' ')
    print(f'Correct answer was \'{result}\'.')
    print(f'Let\'s try again, {name}!')
