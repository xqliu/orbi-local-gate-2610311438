from app import farewell, greet


def test_greet_name():
    assert greet("Ada") == "Hello, Ada"


def test_greet_empty_name_greets_stranger():
    assert greet("") == "Hello, stranger"


def test_greet_none_name_greets_stranger():
    assert greet(None) == "Hello, stranger"


def test_farewell_name():
    assert farewell("Ada") == "Goodbye, Ada"


def test_farewell_empty_name_says_goodbye_to_stranger():
    assert farewell("") == "Goodbye, stranger"


def test_farewell_none_name_says_goodbye_to_stranger():
    assert farewell(None) == "Goodbye, stranger"
