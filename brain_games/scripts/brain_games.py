#!/usr/bin/env python
"""Main program."""

import sys

from brain_games import cli


def main():
    """Add main function."""
    sys.stdout.write('Welcome to the Brain Games!')
    cli.welcome_user()


if __name__ == '__main__':
    main()
