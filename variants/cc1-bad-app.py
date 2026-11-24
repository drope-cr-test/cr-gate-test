"""C-C1 test change: obviously bad code that a real review must flag."""

def run_user_code(user_input: str):
    return eval(user_input)  # noqa: S307 -- intentional test payload
