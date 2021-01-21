"""Game progression."""
import random

from brain_games.brain_engine import decorator_game
from brain_games.scripts import brain_games

greeting = 'What number is missing in the progression?\n'


@decorator_game
def func_progression(*args, **kwargs):
    """Add description function.

    Args:
        args: arg.
        kwargs: kwargs.

    Returns:
        variables.
    """
    list_num = [i for i in range(random.randint(1, 25), 100, random.randint(1, 18))][:10]
    random_num = random.randint(0, len(list_num) - 1)
    answer = list_num[random_num]
    list_num[random_num] = '..'
    question = (' '.join(str(i) for i in list_num))
    return answer, question


def main():
    """Add main function."""
    func_progression(brain_games.main(), greeting)


if __name__ == '__main__':
    main()
