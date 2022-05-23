from constants import *
import itertools


def get_valid_letters(digit : str) -> list:
    return PHONE_PANEL_MAP[digit]


def get_letter_combinations(number : str, lst=[]) -> list:
    if len(number) < 1:
        return lst
    elif len(number) == 1:
        lst.append(get_valid_letters(number))
        return lst
    else:
        lastDigitIndex = len(number) - 1
        get_letter_combinations(number[:lastDigitIndex], lst)
        # Create a list of lists consisting of possibilities for each place of digit
        if len(get_valid_letters(number[lastDigitIndex])) > 0:
            lst.append(get_valid_letters(number[lastDigitIndex]))
        # Get Products of the possibilities
        outputLst = list(itertools.product(*lst))
        return [''.join(letter) for letter in outputLst]


if __name__ == '__main__':
    print(get_letter_combinations('23'))