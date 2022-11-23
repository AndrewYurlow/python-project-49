import prompt
import numexpr as ne
from random import randint, choice
from brain_games.scripts.game_data import data


def ask_question(statement):
    print(f"Question: {statement}")


def get_answer():
    answer = prompt.string("Your answer: ")
    return answer


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def get_correct_answer_br_even(num):
    if is_even(num):
        return "yes"
    else:
        return "no"


def get_correct_answer_br_calc(expression):
    result = ne.evaluate(expression)
    return f"{result}"


def get_rand_num():
    return randint(1, 25)


def find_gcd(first, second):
    while len(first) > 0:
        last_item = first.pop()
        if last_item in second:
            return last_item


def find_divisors(num):
    if num == 1:
        return [1]
    divisors = []
    i = 1
    while i <= num:
        if num % i == 0:
            divisors.append(i)
        i += 1
    return divisors


def get_rand_pair():
    first_number = get_rand_num()
    second_number = get_rand_num()
    return f"{first_number} {second_number}"


def get_gcd(pair):
    nums = pair.split(" ")
    first_number = int(nums[0])
    second_number = int(nums[1])
    first_num_divisors = find_divisors(first_number)
    second_num_divisors = find_divisors(second_number)
    gcd = find_gcd(first_num_divisors, second_num_divisors)
    return f"{gcd}"


def get_rand_arithmetic_expr():
    first_number = get_rand_num()
    second_number = get_rand_num()
    operator = choice(data["operators"])
    return f"{first_number} {operator} {second_number}"
