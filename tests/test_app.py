from app import greet


def test_greet_name():
    assert greet("Ada") == "Hello, Ada"


def test_greet_empty_name_greets_stranger():
    assert greet("") == "Hello, stranger"
