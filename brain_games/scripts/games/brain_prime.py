"""Game simple num."""
import secrets

from brain_games.brain_engine import decorator_game
from brain_games.scripts import brain_games

greeting = 'Answer "yes" if given number is prime. Otherwise answer "no".\n'


def simple_num():
    """Add description function.

    Returns:
        variables.
    """
    num_not_simple = 77
    lst = list(range(2, 100))
    for num in lst:
        if num == 0:
            break
        if num == num_not_simple:
            continue
        for idx in range(2 * num, 100, num):
            lst[idx - 2] = 0
    return list(filter(lambda numb: numb > 0, lst))


@decorator_game
def prime_num(*args, **kwargs):
    """Add description function.

    Args:
        args: arg.
        kwargs: kwargs.

    Returns:
        variables.
    """
    question = secrets.randbelow(100)
    check_prime = 'yes' if question in simple_num() else 'no'

    return check_prime, question


def main():
    """Add main function."""
    prime_num(brain_games.main(), greeting)


if __name__ == '__main__':
    main()
