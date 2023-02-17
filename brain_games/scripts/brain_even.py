#!/usr/bin/env python3
import prompt
from random import randint
from brain_games.cli import welcome_user, answer_incorrect


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        number_ = randint(1, 100)
        print(f'Question: {number_}')
        result = number_ % 2 == 0 and 'yes' or 'no'
        user_answer = prompt.string('Your answer: ')
        if user_answer != result or user_answer not in ['yes', 'no']:
            answer_incorrect(result, user_answer, name)
            break
        else:
            print('Correct!')
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
