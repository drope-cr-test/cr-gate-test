"""Trivial app used by the C-C1 control/test PRs."""

def greet(name: str) -> str:
    return f"hello {name}"


def farewell(name: str) -> str:
    return f"goodbye {name}"


def shout(name: str) -> str:
    return f"HEY {name.upper()}!"
