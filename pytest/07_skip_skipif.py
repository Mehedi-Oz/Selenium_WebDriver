import pytest


def is_even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


def test_even_number():
    result = is_even_or_odd(4)
    print(f"Test for 4: {result}")


@pytest.mark.skip(reason="functionnality not developed")
def test_odd_number():
    result = is_even_or_odd(3)
    print(f"Test for 3: {result}")


feature_available = False


@pytest.mark.skipif(not feature_available, reason="feature not available")
def test_large_even_number():
    result = is_even_or_odd(10000)
    assert result == "Even", "10000 should be even"
