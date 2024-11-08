import sys

NESTED_MORSE = {" ": "/ ",
                "A": ".-",
                "B": "-...",
                "C": "-.-.",
                "D": "-..",
                "E": ".",
                "F": "..-",
                "G": "--.",
                "H": "....",
                "I": "..",
                "J": ".---",
                "K": "-.-",
                "L": ".-..",
                "M": "--",
                "N": "-.",
                "O": "---",
                "P": ".--.",
                "Q": "--.-",
                "R": ".-.",
                "S": "...",
                "T": "-",
                "U": "..-",
                "V": "..-",
                "W": ".--",
                "X": "-..-",
                "Y": "-.--",
                "Z": "--..",
                "1": ".----",
                "2": "..---",
                "3": "...--",
                "4": "....-",
                "5": ".....",
                "6": "-....",
                "7": "--...",
                "8": "---..",
                "9": "----.",
                "0": "-----",
                }


def main():
    """
    program takes a string as an argument and encodes it into Morse Code
    """
    try:
        if len(sys.argv) != 2 or not all(c.isalnum()
                                         or c.isspace() for c in sys.argv[1]):
            raise AssertionError("the arguments are bad")

        text = []
        for c in sys.argv[1].upper():
            text.append(NESTED_MORSE[c])
        result = ' '.join(text)
        return print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
