def add(a, b):
    """두 수를 더합니다."""
    return a + b


def subtract(a, b):
    """첫 번째 수에서 두 번째 수를 뺍니다."""
    return a - b


def multiply(a, b):
    """두 수를 곱합니다."""
    return a * b


def divide(a, b):
    """첫 번째 수를 두 번째 수로 나눕니다. 0으로 나누면 오류를 냅니다."""
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b


if __name__ == "__main__":
    print("10 + 5 =", add(10, 5))
    print("10 - 5 =", subtract(10, 5))
    print("10 * 5 =", multiply(10, 5))
    print("10 / 5 =", divide(10, 5))