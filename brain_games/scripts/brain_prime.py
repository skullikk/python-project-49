#!/usr/bin/env python3
import prompt
from random import randint
from brain_games.cli import welcome_user, answer_incorrect

PRIME_NUMBERS = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                 59, 61, 67, 71, 73, 79, 83, 89, 97)


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(3):
        number_ = randint(1, 100)
        print(f'Question: {number_}')
        result = number_ in PRIME_NUMBERS and 'yes' or 'no'
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
