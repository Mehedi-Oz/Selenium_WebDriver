import pytest


def add_numbers(a, b):
    return a + b


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 4),
        (5, 10, 15),
    ],
)
def test_add_numbers(a, b, expected):
    assert add_numbers(a, b) == expected
