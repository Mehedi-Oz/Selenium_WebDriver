import pytest

@pytest.fixture
def setup_environment():
    print("Setting up environement!")
    yield "Environment is ready for testing"
    print("Tearing down envirnment!")

def test_action(setup_environment):
  print(f"Executing test with fixtures: {setup_environment}")
  assert setup_environment == "Environment is ready for testing"
  
def test_action_two(setup_environment):
  print(f"Executing test two with fixtures: {setup_environment}")
  assert "ready" in setup_environment
