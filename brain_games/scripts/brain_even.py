import prompt
from random import randint


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        number_ = randint(1, 100)
        print(f'Question: {number_}')
        result = number_ % 2 == 0 and 'yes' or 'no'
        user_answer = prompt.string('Your answer: ')
        if user_answer != result or user_answer not in ['yes', 'no']:
            print(f'\'{user_answer}\' is wrong answer ;(.', end=' ')
            print(f'Correct answer was \'{result}\'.')
            print(f'Let\'s try again, {name}!')
            break
        else:
            print('Correct!')
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
