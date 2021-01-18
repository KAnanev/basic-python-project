"""Add function welcome_user."""
import sys

import prompt


def welcome_user():
    """Add Function."""
    name = prompt.string('May I have your name? ')
    sys.stdout.write('Hello, {user}!'.format(user=name))
