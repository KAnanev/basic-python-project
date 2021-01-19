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


def decorator_game(func):
    """Add decorator for game.

    Returns:
        wrapper.

    Parameter:
        func: name.
    """
    def wrapper_game(name):
        count = 0
        while count != 3:
            result_game = func(name)
            if result_game[0] == result_game[1]:
                sys.stdout.write('Correct!\n')
                count += 1
            else:
                sys.stdout.write(
                    "Let's try again, {user}!\n".format(user=name),
                )
                break
        if count == 3:
            sys.stdout.write('Congratulations, {user}!\n'.format(user=name))
    return wrapper_game
