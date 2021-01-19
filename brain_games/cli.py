"""Add function welcome_user."""
import sys

import prompt


def welcome_user():
    """Add function welcome_user.

    Returns:
        name.
    """
    name = prompt.string('May I have your name? \n')
    sys.stdout.write('Hello, {user}!\n'.format(user=name))
    return name


if __name__ == '__main__':
    welcome_user()
