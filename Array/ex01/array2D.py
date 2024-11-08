import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    """
    takes as parameters a 2D array, prints its shape, and returns a
    truncated version of the array based on the provided start and end arguments.
    """

    if not all (isinstance(row, list) for row in family):
        raise AssertionError("Input must be a list of lists")
    
    # Check if all rows have the same length
    row_len = len(family[0])
    if not all(len(row) == row_len for row in family):
        raise AssertionError("All rows must have the same length")
    
    # Convert to a NumPy array for easier slicing
    family_array = np.array(family)
    print(f"My shape is : {family_array.shape}")

    # Slice the array
    new_family = family_array[start:end]
    print(f"My new shape is : {new_family}")

    return new_family.tolist()

