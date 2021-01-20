"""GCD."""
import math
import secrets

from brain_games.brain_engine import decorator_game
from brain_games.scripts import brain_games

greeting = 'Find the greatest common divisor of given numbers.\n'


@decorator_game
def great_num(*args, **kwargs):
    """Add description function.

    Args:
        args: arg.
        kwargs: kwargs.

    Returns:
        variables.
    """
    num_one = secrets.randbelow(100)
    num_two = secrets.randbelow(100)
    question = '{0} {1}'.format(num_one, num_two)
    return math.gcd(num_one, num_two), question


def main():
    """Add main function."""
    great_num(brain_games.main(), greeting)


if __name__ == '__main__':
    main()
