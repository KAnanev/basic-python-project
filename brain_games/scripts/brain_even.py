"""Function check_parity."""
import secrets
import sys

import prompt

from brain_games.cli import decorator_game
from brain_games.scripts import brain_games


@decorator_game
def check_parity(name):
    """Add description function.

    Args:
        name: name.

    Returns:
        variables.
    """
    question = secrets.randbelow(100)
    check_even = 'yes' if question % 2 == 0 else 'no'
    sys.stdout.write(
        'Answer "yes" if a number is even, otherwise answer "no".\n',
    )
    sys.stdout.write('Question: {num}\n'.format(num=question))
    answer = prompt.string('Your answer: ')
    return check_even, answer


def main():
    """Add main function."""
    check_parity(brain_games.main())


if __name__ == '__main__':
    main()
