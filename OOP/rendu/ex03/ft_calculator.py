class calculator:
    """A class for performing scalar operations (addition, subtraction,
    on vectors reprensented as list of floats)"""

    def __init__(self, vector) -> None:
        """Initializes the calculator with a vector of numbers.

        Args:
            vector (list): Alist of numbers (floats or integers).
        """
        try:
            if not all(isinstance(x, (int, float)) for x in vector):
                raise ValueError("All elements of the vector must be\
                                integers or floats.")
            self.vector = vector
        except Exception as e:
            print(f"Error: {e}")

    def __add__(self, scalar) -> None:
        """Adds a scalar to each elemnt of the vector.

        Args:
            scalar (int or float): The scalar to be added.
        """
        try:
            if not isinstance(scalar, (int, float)):
                raise ValueError("Scalar must be an integer or float.")
            self.vector = [x + scalar for x in self.vector]
            print(self.vector)
        except Exception as e:
            print(f"Error during addition: {e}")

    def __mul__(self, scalar):
        """Multiplies each element of the vector by a scalar.

        Args:
            scalar (int or float): The scalar multiplier.
        """
        try:
            if not isinstance(scalar, (int, float)):
                raise ValueError("Scalar must be an integer or float.")
            self.vector = [x * scalar for x in self.vector]
            print(self.vector)
        except Exception as e:
            print(f"Error during multiplacation: {e}")

    def __sub__(self, scalar):
        """Subtract a scalar from each elemnt of vector.

        Args:
            scalar (int,float): The scalar divisor.
        """
        try:
            if not isinstance(scalar, (int, float)):
                raise ValueError("Scalar must be an integer or float.")
            self.vector = [x - scalar for x in self.vector]
            print(self.vector)
        except Exception as e:
            print(f"Error during subtraction: n{e}")

    def __truediv__(self, scalar):
        """Divides each elemnt of the vector by a scalar.

        Args:
            scalar (int, float): The scalar divisor
        """
        try:
            if not isinstance(scalar, (int, float)):
                raise ValueError("Scalar must be an int or float.")
            if scalar == 0:
                raise ZeroDivisionError("Division by zero not allowed.")
            self.vector = [x / scalar for x in self.vector]
            print(self.vector)
        except ZeroDivisionError as ve:
            print(f"ZeroDivisionError: {ve}")
        except Exception as e:
            print(f"Error during division: {e}")
