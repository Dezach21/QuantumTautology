class ReadOnly:
    """Make constants read-only."""

    def __init__(self, value: float) -> None:
        self._value = value

    def __get__(self, instance, owner) -> float:
        return self._value

    def __set__(self, instance, value) -> None:
        raise AttributeError(f"Cannot modify a read-only constant.")


# --- Constants --- #

class _Constants:
    e = ReadOnly(2.71828182845904523536)
    pi = ReadOnly(3.14159265358979323846)


def _const_setattr() -> None:
    raise AttributeError("Cannot modify a read-only constant.")


constants = _Constants()
constants.__class__.__setattr__ = _const_setattr


# Euler's number.
e = constants.e

# Pi.
pi = constants.pi


# --- Basic functions --- #

def sqrt(x: int | float | complex) -> float | complex:
    return x ** 0.5


def exp(x: int | float | complex) -> float | complex:
    """
    Exponentiation base `e`.

    :param x: Exponent.
    :return: `e^x`.
    """
    return e ** x


def factorial(x: int) -> int:
    """
    Factorial.

    :param x: Value.
    :return: `x!`.
    """
    if type(x) is not int:
        raise TypeError("Argument must be an integer.")
    if x < 0:
        raise ValueError("Argument must be positive.")
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)


# --- Distributions --- #

def gaussian(x: int | float, mu: int | float, sigma: int | float) -> float:
    """
    Normalized Gaussian function.

    :param x: Value to evaluate at.
    :param mu: Mean of the Gaussian.
    :param sigma: Standard deviation of the Gaussian.
    :return: Evaluated value.
    """
    return exp(((x - mu) / sigma) ** 2 / -2) / (sigma * sqrt(2 * pi))
