import pytest

def add_numbers(a, b):
    return a / b

@pytest.mark.xfail(reason="Divide by zero is not handlede", strict=True)
def test_divide_by_zero():
    assert divide(1, 0) == 0

@pytest.mark.xfail(condition=True, reason="Known Bug")
def test_sub_bug():
    result = 5 - 3
    assert result == 1

