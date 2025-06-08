import pytest


def is_even_or_odd_new(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


def test_even_number_new():
    result = is_even_or_odd_new(4)
    print(f"Test for 4: {result}")


def test_odd_number_new():
    result = is_even_or_odd_new(3)
    print(f"Test for 3: {result}")


@pytest.mark.regression
def test_large_even_number_new():
    result = is_even_or_odd_new(10000)
    assert result == "Even", "10000 should be even"
