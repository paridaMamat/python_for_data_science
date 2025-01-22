def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Calculates statistics based on the provided arguments and
    keyword arguments.

    Supported operations:
        - mean
        - median
        - quartile
        - std (standard deviation)
        - var (variance)
    """

    def mean(data):
        """
        Calculates the mean of the values in the list and returns
        it.
        """
        return sum(data) / len(data)

    def median(data):
        """
        Calculates the median of the values in the list and returns
        it.
        """
        sorted_data = sorted(data)
        n = len(data)
        if n % 2 == 0:
            mid = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        else:
            mid = sorted_data[n // 2]
        return mid

    def quartile(data):
        """
        Calculates the first and third quartiles of the values
        in the list and returns them.

        Parameters:
            - values (list): A sorted list of numbers.
            - len_vals (int): The length of the list.

        Returns:
            float: The first and third quartiles of the values in
            the list.
        """

        values = sorted(data)
        len_vals = len(values)
        q1_index = len_vals // 4
        q3_index = len_vals * 3 // 4

        if len_vals % 4 == 0:
            q1 = (values[q1_index - 1] + values[q1_index]) / 2
            q3 = (values[q3_index - 1] + values[q3_index]) / 2
        else:
            q1 = values[q1_index]
            q3 = values[q3_index]

        return [float(q1), float(q3)]

    def var(data) -> float:
        """
        Calculates the variance of the values in the list and
        returns it.
        """
        mean_data = mean(data)
        return sum((x - mean_data) ** 2 for x in data) / len(data)

    def std(data) -> float:
        """
        Calculates the standard deviation of the values in the
        list
        and stores it in the dictionary d_results
        """
        return var(data) ** 0.5

    # Supported operations
    supported_operations = {
        "mean": mean,
        "median": median,
        "quartile": quartile,
        "std": std,
        "var": var
    }

    # Process kwargs for requested statistics
    for key, operation in kwargs.items():
        try:
            assert len(args) > 0, "ERROR"
            if not all(isinstance(arg, (int, float)) for arg in args):
                raise ValueError("All positional arguments must be numbers.")
            if operation in supported_operations:
                result = supported_operations[operation](list(args))
                print(f"{operation} : {result}")

        except AssertionError as e:
            print(e)
        except Exception as e:
            print("Exception:", e)
