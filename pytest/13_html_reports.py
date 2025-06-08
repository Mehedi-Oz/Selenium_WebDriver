def test_add():
    result = 2 + 3
    print(f"Result of  2 + 3 is: {result}")
    assert result==5


def test_sub():
    result = 13 - 3
    print(f"Result of 13 - 3 is: {result}")
    assert result==10

def test_fail():
    result = 13 - 2
    print(f"Result of 13 - 2 is: {result}")
    assert result==10

