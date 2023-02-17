#!/usr/bin/env python3
import prompt
from random import randint
from brain_games.cli import welcome_user, answer_incorrect


def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    for i in range(3):
        number_1 = randint(1, 10)
        number_2 = randint(1, 10)
        print(f'Question: {number_1} {number_2}')
        result = gcd(number_1, number_2)
        user_answer = prompt.integer('Your answer: ')
        if user_answer != result:
            answer_incorrect(result, user_answer, name)
            break
        else:
            print('Correct!')
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
