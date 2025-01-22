def callLimit(limit: int):
    """
    This function is a decorator that limits the number of times a function
    can be called.
    The limit is the number of times the function can be called.
    returns:
        function that limits the number of times a function can be called.
    """
    def callLimiter(function):
        """
        This function returns a function that limits the number of times
        a function can be called.
        """
        count = 0

        def limit_function(*args: any, **kwds: any):
            """
            This function limits the number of times a function can be called.
            It returns the result of the function if it is called fewer times
            than the limit, otherwise it prints an error message.
            """
            nonlocal count
            try:
                assert limit > 0, "Error: Limit must be greater than 0"
                assert count < limit, f"Error: {function} called too many\
                times"
                count += 1
                return function(*args, **kwds)
            except AssertionError as e:
                print(e)
        return limit_function
    return callLimiter
