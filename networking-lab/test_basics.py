##test_basics.py

def test_addition():
    result = 10+20
    try:
        assert result ==40
    finally:
        print("Cleaning up!")