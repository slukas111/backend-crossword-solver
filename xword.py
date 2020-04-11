#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "Sasha Lukas"

# YOUR HELPER FUNCTION GOES HERE
def helper_function(test_word, dict):
    word_check = len(test_word)-test_word.count(' ')
    for word in dict:
        letter = 0
        match = 0
        if len(word) == len(test_word):
            for letter in test_word:
                match += 1
            else:
                letter += 1


def main():
    with open('dictionary.txt', 'r') as f:
        words = f.read().split()
        f.close()
        return words


    test_word = raw_input (
        'Please enter a word to solve.\nUse spaces to signify unknown letters: ').lower()

    # YOUR ADDITIONAL CODE HERE
    raise NotImplementedError('Please complete this')


if __name__ == '__main__':
    main()
