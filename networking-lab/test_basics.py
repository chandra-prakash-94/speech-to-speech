##test_basics.py
import pytest

@pytest.fixture
def sample_user():
    print("Setup")
    yield "Bob"
    print("Clean up")

def test_username(sample_user):
    assert sample_user=="Bob"

def test_addition():
    result = 10+20
    try:
        assert result ==30
    finally:
        print("Cleaning up!")