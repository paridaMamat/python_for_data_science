class calculator:
    """A class to perform vector operations: dot product, addition,\
        and subtraction."""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calcualte the dot product of two vector and print the result.
        Args:
            V1 (list [float]): First vector
            V2 (list[float]): Second vector
        """
        result = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is : {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Add two vector element-wise and print the result.
        Args:
            V1 (list[folat]): First vector
            V2 (list[float]): Second vector
        """
        result = [float(x) + float(y) for x, y in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtract two vector elemnt-wise and print result.
        Args:
            V1 (list[float]): First vector
            V2 (list[float]): Second vector
        """
        result = [float(x) - float(y) for x, y in zip(V1, V2)]
        print(f"Sous vector is: {result}")
