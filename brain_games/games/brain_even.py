#!/usr/bin/env python3
from brain_games.scripts.brain_games import main as greet_user
from brain_games.scripts import game_functions as gf


def main():
    greet_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    gf.start(gf.get_rand_num, gf.get_correct_answer_br_even)


if __name__ == "__main__":
    main()
