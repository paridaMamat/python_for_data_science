import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    take 2 lists of integers or floats in input and returns a list
    of BMI values
    it will return error if list of height and  weight are not has in same size, and if there is a value negatif or zero
    """
    if len(height) != len(weight):
        raise ValueError("Height and Weight list should have same size")
    if not all(isinstance(h, (int, float)) and h > 0 for h in height):
        raise ValueError("All height values must be positive integers or floats.")
    if not all(isinstance(w, (int, float)) and w > 0 for w in weight):
        raise ValueError("All weight values must be positive integers or floats.")
    
    height_arr = np.array(height)
    weight_arr = np.array(weight)

    bmi = weight_arr / (height_arr * height_arr)
    return bmi.tolist()



def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    accepts a list of integers or floats and an integer representing
    a limit as parameters. It returns a list of booleans (True if above the limit)
    """
    if not bmi:
        raise AssertionError("Error: BMI array is empty or invalid.")
    return [h > limit for h in bmi]
    


