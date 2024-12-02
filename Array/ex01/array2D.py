import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    takes as parameters a 2D array, prints its shape, and returns a
    truncated version of the array based on the provided start and \
        end arguments.
    """
    try:
        if not all(isinstance(row, list) for row in family):
            raise AssertionError("Input must be a list of lists")

        # Check if all rows have the same length
        row_len = len(family[0])
        if not all(len(row) == row_len for row in family):
            raise AssertionError("All rows must have the same length")

        # Validate that start and end are integers
        if not isinstance(start, int) or not isinstance(end, int):
            raise ValueError("Start and end indices must be integers")

        # Convert to a NumPy array for easier slicing
        family_array = np.array(family)
        print(f"My shape is : {family_array.shape}")

        # Slice the array
        new_family = family_array[start:end]
        print(f"My new shape is : {new_family.shape}")

        return new_family.tolist()
    except AssertionError as ae:
        print(f"AssertionError: {ae}")
        return []
    except ValueError as ve:
        print(f"ValueError: {ve}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
