#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "Sasha Lukas"

# YOUR HELPER FUNCTION GOES HERE


def main():
    with open('dictionary.txt', 'r') as f:
        words = f.read().split()
        f.close()
        return words
        print(words)

    test_word = raw_input(
        'Please enter a word to solve.\nUse spaces to signify unknown letters: ').lower()

    # YOUR ADDITIONAL CODE HERE
    raise NotImplementedError('Please complete this')


if __name__ == '__main__':
    main()
