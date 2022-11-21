#!/usr/bin/env python3
from brain_games.scripts.brain_games import main as greet_user
from brain_games.scripts import game_functions as gf


def main():
    greet_user()
    print('What is the result of the expression?')
    gf.start(gf.get_rand_arithmetic_expr, gf.get_correct_answer_br_calc)


if __name__ == "__main__":
    main()
