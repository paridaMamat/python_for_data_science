from ft_filter import ft_filter


def is_even(num):
    return num % 2 == 0


def test_filter():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    strings = ["apple", "banana", "cherry", "date", "elderberry"]
    mixed_types = [1, "apple", 2.5, "banana", 3, "cherry", 4.7]

    # Test 1: Compare ft_filter with filter for even numbers
    even_numbers_ft = ft_filter(is_even, numbers)
    even_numbers_filter = filter(is_even, numbers)
    assert list(even_numbers_ft) == list(even_numbers_filter), \
        "\033[31mTest 1 failed\033[0m"
    print("\033[32m       ok\033[0m")

    # Test 2: Compare ft_filter with filter for odd numbers
    odd_numbers_ft = ft_filter(lambda x: x % 2 != 0, numbers)
    odd_numbers_filter = filter(lambda x: x % 2 != 0, numbers)
    assert list(odd_numbers_ft) == list(odd_numbers_filter), \
        "\033[31mTest 2 failed\033[0m"
    print("\033[32m       ok\033[0m")

    # Test 3: Compare ft_filter with filter for numbers greater than 5
    greater_than_5_ft = ft_filter(lambda x: x > 5, numbers)
    greater_than_5_filter = filter(lambda x: x > 5, numbers)
    assert list(greater_than_5_ft) == list(greater_than_5_filter), \
        "\033[31mTest 3 failed\033[0m"
    print("\033[32m       ok\033[0m")

    # Test 4: Compare ft_filter with filter for strings longer than 5 characters
    long_strings_ft = ft_filter(lambda s: len(s) > 5, strings)
    long_strings_filter = filter(lambda s: len(s) > 5, strings)
    assert list(long_strings_ft) == list(long_strings_filter), \
        "\033[31mTest 4 failed\033[0m"
    print("\033[32m       ok\033[0m")

    # Test 5: Compare ft_filter with filter for integers in mixed types
    integers_ft = ft_filter(lambda x: isinstance(x, int), mixed_types)
    integers_filter = filter(lambda x: isinstance(x, int), mixed_types)
    assert list(integers_ft) == list(integers_filter), \
        "\033[31mTest 5 failed\033[0m"
    print("\033[32m       ok\033[0m")

    # Test 6: Compare ft_filter with filter for floats in mixed types
    floats_ft = ft_filter(lambda x: isinstance(x, float), mixed_types)
    floats_filter = filter(lambda x: isinstance(x, float), mixed_types)
    assert list(floats_ft) == list(floats_filter), \
        "\033[31mTest 6 failed\033[0m"
    print("\033[32m       ok\033[0m")

    print("\033[32mAll tests passed\033[0m")


test_filter()