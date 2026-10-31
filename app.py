def greet(name: str | None) -> str:
    return f"Hello, {name or 'stranger'}"
