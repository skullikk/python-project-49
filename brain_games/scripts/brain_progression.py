#!/usr/bin/env python3
import prompt
from random import randint
from brain_games.cli import welcome_user, answer_incorrect


def progression():
    start = randint(1, 10)
    lenght = randint(5, 10)
    step = randint(2, 10)
    index = randint(0, lenght - 1)
    stop = start + lenght * step
    list_ = list(range(start, stop, step))
    number_ = list_[index]
    list_[index] = '..'
    print('Question: ', end='')
    print(*list_, sep=' ')
    return number_


def main():
    name = welcome_user()
    print('What number is missing in the progression?')
    for i in range(3):
        result = progression()
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
