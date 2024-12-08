from math import *


class QuantumState:
    def __init__(self, state) -> None:
        self.state = state
        self.normalize()

    def __repr__(self) -> repr:
        return repr(self.state)

    def normalize(self) -> None:
        """Normalize the state to 1."""
        norm = sqrt(sum(abs(amplitude) ** 2 for amplitude in self.state))
        if norm != 0:
            self.state = [amplitude / norm for amplitude in self.state]

    def probability(self) -> list:
        """Probability distribution of the wave function amplitude."""
        return [abs(amplitude) ** 2 for amplitude in self.state]

    @staticmethod
    def initialize_gaussian(n: int, mu: int | float, sigma: int | float) -> "QuantumState":
        """
        Initialize a Gaussian wave function.

        :param n: Number of points in the wave function.
        :param mu: Mean of the Gaussian.
        :param sigma: Standard deviation of the Gaussian.
        :return: A wave function with a Gaussian probability distribution.
        """
        return QuantumState([gaussian(x, mu, sigma) for x in range(n)])

    @staticmethod
    def initialize_uniform(n: int) -> "QuantumState":
        """
        Initialize a uniform wave function (equal probability).

        :param n: Number of points in the wave function.
        :return: A wave function with a uniform probability distribution.
        """
        return QuantumState([1] * n)
