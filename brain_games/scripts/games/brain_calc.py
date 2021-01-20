"""Calculator."""

import secrets
from random import choices

from brain_games.brain_engine import decorator_game
from brain_games.scripts import brain_games

greeting = 'What is the result of the expression?.\n'
exit_text = 'is wrong answer ;(. Correct answer was'


@decorator_game
def func_calc(*args, **kwargs):
    """Add description function.

    Args:
        args: arg.
        kwargs: kwargs.

    Returns:
        variables.
    """
    num_one = secrets.randbelow(100)
    num_two = secrets.randbelow(100)
    dict_operators = {
        '+': num_one.__add__(num_two),
        '-': num_one.__sub__(num_two),
        '*': num_one.__mul__(num_two),
    }
    operation_sign = choices(list(dict_operators.items()))
    question = '{0}{1}{2}'.format(num_one, operation_sign[0][0], num_two)
    return operation_sign[0][1], question


def main():
    """Add main function."""
    func_calc(brain_games.main(), greeting, exit_text)


if __name__ == '__main__':
    main()
