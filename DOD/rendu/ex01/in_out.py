def square(x: int | float) -> int | float:
    """Returns the square of the given number."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Returns the number raised to the power of itself."""
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Return an object that when called return the result of the function

    parameters:
        x (int | float) : The number to calculate.
        function (function) : The fuction to use for the calculation.

    return :
        object: The object that when called return the result of the function.
    """
    count = 0
    try:
        assert isinstance(x, (int, float)), "The input must be an\
        integer or a float."
        assert callable(function), "The function must be callable."

        def inner() -> float:
            nonlocal count
            nonlocal x
            x = function(x)
            count += 1
            return x

        return inner
    except AssertionError as e:
        return e
