from app import greet


def test_greet_name():
    assert greet("Ada") == "Hello, Ada"
