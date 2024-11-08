import sys
import re


def main():
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    try:

        # Check the number of arguments and their types
        if len(sys.argv) != 3 or not isinstance(sys.argv[1], str)\
                or not sys.argv[2].isdigit():
            raise AssertionError("the arguments are bad")

        # Extract arguments
        s = sys.argv[1]
        n = int(sys.argv[2])

        # Check if the string contains any special characters
        if re.search(r'[^a-zA-Z0-9 ]', s):
            raise AssertionError("The string contains special characters")

        # Use list comprehension to filter words by length
        result = list(filter(lambda word: len(word) > n, s.split()))

        # Print the result
        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
