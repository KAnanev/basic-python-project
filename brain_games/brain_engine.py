"""Engine games."""
import sys

import prompt


def break_point(name):
    """Add break function."""
    sys.stdout.write(
        "Let's try again, {user}!\n".format(user=name),
    )


def decorator_game(func):
    """Add decorator for game.

    Returns:
        wrapper.

    Parameter:
        func: name.
    """

    def wrapper_game(name, greeting_text, exit_text=None):
        count = 0
        while count != 3:
            result_game = func(name, greeting_text, exit_text=None)
            sys.stdout.write(greeting_text)
            sys.stdout.write('Question: {num}\n'.format(num=result_game[1]))
            answer = prompt.string('Your answer: ')
            if str(result_game[0]) == answer:
                sys.stdout.write('Correct!\n')
                count += 1
            elif exit_text:
                sys.stdout.write(
                    '{0} {1} {2}.\n'.format(
                        answer,
                        exit_text,
                        result_game[0],
                    ),
                )
                break_point(name)
                break
            else:
                break_point(name)
                break
        if count == 3:
            sys.stdout.write('Congratulations, {user}!\n'.format(user=name))

    return wrapper_game
