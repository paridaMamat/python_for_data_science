import sys

def main():
    """
    Checks if an integer argument is provided. Prints "I'm Even." or "I'm Odd."
    Handles potential errors gracefully.
    """
    try:
        if len(sys.argv) == 1:
            # No argument provided, do nothing
            return
        elif len(sys.argv) > 2:
            raise AssertionError("AssertionError: More than one argument is provided.")

        # Try to convert the argument to an integer
        number = int(sys.argv[1])

        # Check if the number is even or odd
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    
    except AssertionError as e:
        print(e)  # Only print the error message, no traceback
    except ValueError:
        print("AssertionError: argument is not an integer")

if __name__ == "__main__":
    main()