def greet(name: str | None) -> str:
    return f"Hello, {name or 'stranger'}"


def farewell(name: str | None) -> str:
    return f"Goodbye, {name or 'stranger'}"
