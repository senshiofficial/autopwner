def letter_score(letter: str) -> int:
    '''Function to return the score of a given letter in scrabble according to

    :param letter: Char to find the score of
    :type letter: String

    :rtype: Integer
    '''

    match letter.lower():
        case "a" | "d" | "e" | "i" | "n" | "o" | "r" | "s" | "t":
            return 1

        case "g" | "h" | "l":
            return 2

        case "b" | "c" | "m" | "p":
            return 3

        case "j" | "k" | "u" | "v" | "w":
            return 4

        case "f":
            return 5

        case "z":
            return 6

        case "x" | "y":
            return 8

        case "q":
            return 10

        case _:
            return 0


def scrabble_score(s: str) -> int:
    '''Calculate the scrabble score of a given word

    :param s: Word to calculate score of
    :type s: String

    :rtype: Integer
    '''

    if len(s) == 0:
        return 0

    return letter_score(s[0]) + scrabble_score(s[1:])