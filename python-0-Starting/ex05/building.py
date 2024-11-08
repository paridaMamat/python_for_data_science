import sys
import string


def count_characters(text):
    """
    Count the number of upper-case letters, lower-case letters, \
        punctuation marks, digits, and spaces in the given text.

    Parameters:
    text (str): The string to be analyzed.

    Returns:
    None
    """
    upper = 0
    lower = 0
    digit = 0
    space = 0
    punc = 0

    for char in text:
        if char.isdigit():
            digit += 1
        elif char.isspace():
            space += 1
        elif char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char in string.punctuation:
            punc += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punc} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def main():
    """
    The main function of the script, which handles user input and \
          invokes the count_characters function.

    Parameters:
    None

    Returns:
    None
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("Only one argument accepted")
        elif len(sys.argv) == 1:
            try:
                text = input("What is the text to count?\n")
            except EOFError:
                print("\nInput ended unexpectedly. No text was provided.")
                sys.exit(1)
        else:
            text = sys.argv[1]

        count_characters(text)
    except AssertionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occured: {e}")


if __name__ == "__main__":
    main()
