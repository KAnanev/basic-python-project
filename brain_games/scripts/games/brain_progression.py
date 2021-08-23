"""Game progression."""
import secrets

from brain_games.brain_engine import decorator_game
from brain_games.scripts import brain_games

greeting = 'What number is missing in the progression?\n'


def list_nums():
    """Add description function.

    Returns:
        variables.
    """
    random_num = secrets.SystemRandom()
    
    max_num = random_num.randrange(1, 11)
    num = random_num.randrange(1, 11)
    num_start = secrets.randbelow(max_num)
    num_step = secrets.randbelow(num)
    return list(range(num_start, 100, num_step))[:10]


@decorator_game
def func_progression(*args, **kwargs):
    """Add description function.

    Args:
        args: arg.
        kwargs: kwargs.

    Returns:
        variables.
    """
    list_num = list_nums()
    random_num = secrets.randbelow(len(list_num))
    answer = list_num[random_num]
    list_num[random_num] = '..'
    question = (' '.join(str(itm) for itm in list_num))
    return answer, question


def main():
    """Add main function."""
    func_progression(brain_games.main(), greeting)


if __name__ == '__main__':
    main()
