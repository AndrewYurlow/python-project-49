#!/usr/bin/env python3
from brain_games.scripts.brain_games import main as greet_user
from brain_games.scripts.game_logic import start
from brain_games.scripts.game_utils import get_rand_pair, get_gcd


def main():
    greet_user()
    print('Find the greatest common divisor of given numbers.')
    start(get_rand_pair, get_gcd)


if __name__ == "__main__":
    main()
