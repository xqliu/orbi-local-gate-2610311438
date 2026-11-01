from app import greet


def test_greet_name():
    assert greet("Ada") == "Hello, Ada"


def test_greet_empty_name_greets_stranger():
    assert greet("") == "Hello, stranger"


def test_greet_none_name_greets_stranger():
    assert greet(None) == "Hello, stranger"


def test_farewell_named():
    from app import farewell
    assert farewell("Ada") == "Goodbye, Ada"


def test_farewell_stranger():
    from app import farewell
    assert farewell(None) == "Goodbye, stranger"
    assert farewell("") == "Goodbye, stranger"
