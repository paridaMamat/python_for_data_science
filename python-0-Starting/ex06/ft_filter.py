
def ft_filter(function, iterable):
    """
    function returns an iterator where the items are filtered \
        through a function to test if the item is accepted or not.

    parameters:
        function: function that tests if each element of a sequence \
            is true or not.
        sequence: sequence which needs to be filtered, it can be sets,\
            lists, tuples, or containers of any iterators.

    Returns: an iterator that is already filtered.
    """
    try:
        iter(iterable)
    except TypeError:
        raise TypeError(f"{type(iterable).__name__} object is not iterable")

    # If function is None, filter truthy values
    if function is None:
        return (item for item in iterable if item)

    # Otherwise, filter using the provided function
    else:
        def safe_function(item):
            try:
                result = function(item)
                # Ensure the result is boolean-convertible
                if not isinstance(result, bool):
                    raise TypeError(f"The function did not return a boolean\
                                     for item: {item}")
                return result
            except Exception as e:
                # Catch any other unexpected errors from the function
                raise RuntimeError(f"An error occurred while processing \
                                   item {item}: {e}")

        return (item for item in iterable if safe_function(item))
