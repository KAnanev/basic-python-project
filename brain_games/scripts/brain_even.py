"""Function check_parity."""
import secrets
import sys

import prompt

from brain_games.scripts import brain_games


def check_even(num):
    """Add function even.

    Args:
        num: number.

    Returns:
        yes or no.
    """
    return 'yes' if num % 2 == 0 else 'no'


def check_parity(name):
    """Add description function.

    Args:
        name: name.
    """
    count = 0
    while count != 3:
        question = secrets.randbelow(100)
        sys.stdout.write(
            'Answer "yes" if a number is even, otherwise answer "no".\n',
        )
        sys.stdout.write('Question: {num}\n'.format(num=question))
        answer = prompt.string('Your answer: ')

        if check_even(question) == answer:
            sys.stdout.write('Correct!\n')
            count += 1
        else:
            sys.stdout.write('Let"s try again, {user}!\n'.format(user=name))
            break

    if count == 3:
        sys.stdout.write('Congratulations, {user}!\n'.format(user=name))


def main():
    """Add main function."""
    check_parity(brain_games.main())


if __name__ == '__main__':
    main()
