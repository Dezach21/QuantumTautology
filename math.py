# --- Constants --- #

# Euler's number.
E = 2.71828182845904523536

# Pi.
PI = 3.14159265358979323846


# --- Basic functions --- #

def sqrt(x: int | float | complex) -> float | complex:
    return x ** 0.5


def exp(x: int | float | complex) -> float | complex:
    """
    Exponentiation base `e`.

    :param x: Exponent.
    :return: `e^x`.
    """
    return E ** x


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


# --- Trigonometric functions --- #

def sin(x: int | float | complex) -> complex:
    """
    Sine.

    :param x: Value.
    :return: `sin(x)`.
    """
    return (exp(1j * x) - exp(-1j * x)) / 2j


def cos(x: int | float | complex) -> complex:
    """
    Cosine.

    :param x: Value.
    :return: `cos(x)`.
    """
    return (exp(1j * x) + exp(-1j * x)) / 2


# --- Distributions --- #

def gaussian(x: int | float, mu: int | float, sigma: int | float) -> float:
    """
    Normalized Gaussian function.

    :param x: Value to evaluate at.
    :param mu: Mean of the Gaussian.
    :param sigma: Standard deviation of the Gaussian.
    :return: Evaluated value.
    """
    return exp(((x - mu) / sigma) ** 2 / -2) / (sigma * sqrt(2 * PI))
