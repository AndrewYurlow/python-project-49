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
    return randint(data['rand_start'], data['rand_end'])


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


def get_progression():
    step = randint(data['progression_step_start'], data['progression_step_end'])
    length = data['progression_len']
    hidden_elem_index = randint(0, length - 1)
    progression = ''
    current_number = get_rand_num()
    i = 0
    while i < length:
        if i == hidden_elem_index:
            progression += ".. "
        else:
            progression += f"{current_number} "
        current_number += step
        i += 1
    return progression


def get_hidden_number(progression):
    arr = progression.strip().split(' ')
    hidden_num_index = arr.index('..')
    first_half = arr[:hidden_num_index]
    second_half = arr[hidden_num_index + 1:] if hidden_num_index != len(arr) - 1 else []
    arr_half = first_half if len(first_half) > len(second_half) else second_half
    step = int(arr_half[1]) - int(arr_half[0])
    num = 0
    if len(second_half) != 0:
        num = int(second_half[0]) - step
    else:
        num = int(first_half[len(first_half) - 1]) + step
    return f"{num}"
