#!/usr/bin/env python3
import prompt
from random import randint, choice
from brain_games.cli import welcome_user, answer_incorrect


def main():
    name = welcome_user()
    signs = ['+', '-', '*']
    print('What is the result of the expression?')
    for _ in range(3):
        number_1 = randint(1, 10)
        number_2 = randint(1, 10)
        sign = choice(signs)
        print(f'Question: {number_1} {sign} {number_2}')
        if sign == '+':
            result = number_1 + number_2
        elif sign == '-':
            result = number_1 - number_2
        else:
            result = number_1 * number_2
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
