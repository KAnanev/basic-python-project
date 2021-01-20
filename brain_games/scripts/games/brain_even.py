"""Function check_parity."""
import secrets

from brain_games.brain_engine import decorator_game
from brain_games.scripts import brain_games

greeting = 'Answer "yes" if a number is even, otherwise answer "no".\n'


@decorator_game
def check_parity(*args, **kwargs):
    """Add description function.

    Args:
        args: arg.
        kwargs: kwargs.

    Returns:
        variables.
    """
    question = secrets.randbelow(100)
    check_even = 'yes' if question % 2 == 0 else 'no'

    return check_even, question


def main():
    """Add main function."""
    check_parity(brain_games.main(), greeting)


if __name__ == '__main__':
    main()
