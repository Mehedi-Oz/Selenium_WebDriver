import pytest

@pytest.fixture(params=["Chrome", "Firefox", "Edge"])
def browser(request):
    return request.param

def test_browser_launch(browser):
    print(f"Running Test on: {browser}")
    assert browser in ["Chrome", "Firefox", "Edge"]
