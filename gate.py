from QuantumTautology.math import PI, sqrt, exp, sin, cos
from QuantumTautology.matrix import Matrix, identity_matrix, embed


class QuantumGates(Matrix):
    # --- Identity gates --- #

    @staticmethod
    def i() -> Matrix:
        """Identity gate."""
        return identity_matrix(2)

    @staticmethod
    def ph(angle: int | float) -> Matrix:
        """
        Global phase gate.

        :param angle: Phase shift angle in radians.
        """
        return identity_matrix(2) * exp(1j * angle)

    # --- Clifford qubit gates --- #

    # - Pauli - #

    @staticmethod
    def x() -> Matrix:
        """Pauli X gate."""
        return Matrix([[0, 1],
                       [1, 0]])

    @staticmethod
    def y() -> Matrix:
        """Pauli Y gate."""
        return Matrix([[0, -1],
                       [1, 0]]) * 1j

    @staticmethod
    def z() -> Matrix:
        """Pauli Z gate."""
        return Matrix([[1, 0],
                       [0, -1]])

    # - Pauli square roots - #

    @staticmethod
    def sx() -> Matrix:
        """Square root of X."""
        return Matrix([[1 + 1j, 1 - 1j],
                       [1 - 1j, 1 + 1j]]) / 2

    @staticmethod
    def sy() -> Matrix:
        """Square root of Y."""
        return Matrix([[0, 1 - 1j],
                       [1 + 1j, 0]]) / sqrt(2)

    @staticmethod
    def sz() -> Matrix:
        """Square root of Z."""
        return Matrix([[1, 0],
                       [0, 1j]])

    # - Hadamard - #

    @staticmethod
    def h() -> Matrix:
        """Hadamard gate."""
        return Matrix([[1, 1],
                       [1, -1]]) / sqrt(2)

    # - Controlled gates - #

    @staticmethod
    def cx() -> Matrix:
        """Controlled not gate."""
        return embed(QuantumGates.x(), 4)

    @staticmethod
    def acx() -> Matrix:
        """Anti-controlled not gate."""
        return Matrix([[0, 1, 0, 0],
                       [1, 0, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])

    @staticmethod
    def dcx() -> Matrix:
        """Double-controlled not gate."""
        return Matrix([[1, 0, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1],
                       [0, 1, 0, 0]])

    @staticmethod
    def cy() -> Matrix:
        """Controlled Y gate."""
        return embed(QuantumGates.y(), 4)

    @staticmethod
    def cz() -> Matrix:
        """Controlled Z gate."""
        return embed(QuantumGates.z(), 4)

    @staticmethod
    def cu(operation_gate: Matrix) -> Matrix:
        """
        Controlled U gate.

        :param operation_gate: `U` gate that operates on a single qubit.
        """
        return embed(operation_gate, 4)

    # - Swap gates - #

    @staticmethod
    def s() -> Matrix:
        """Swap gate."""
        return Matrix([[1, 0, 0, 0],
                       [0, 0, 1, 0],
                       [0, 1, 0, 0],
                       [0, 0, 0, 1]])

    @staticmethod
    def ims() -> Matrix:
        """Imaginary swap gate."""
        return Matrix([[1, 0, 0, 0],
                       [0, 0, 1j, 0],
                       [0, 1j, 0, 0],
                       [0, 0, 0, 1]])

    # --- Non-Clifford qubit gates --- #

    # - Phase gates - #

    @staticmethod
    def p(angle: int | float) -> Matrix:
        """
        Phase shift gate.

        :param angle: Phase shift angle in radians.
        """
        return embed(exp(1j * angle), 2)

    @staticmethod
    def cp(angle: int | float) -> Matrix:
        """
        Controlled phase gate.

        :param angle: Phase shift angle in radians.
        """
        return embed(exp(1j * angle), 4)

    @staticmethod
    def csz() -> Matrix:
        """Controlled square root of Z gate."""
        return embed(1j, 4)

    # - Rotation gates - #

    @staticmethod
    def rx(angle: int | float) -> Matrix:
        """
        Rotation about x-axis gate.

        :param angle: Phase shift angle in radians.
        """
        theta = angle / 2
        c, s = cos(theta), -1j * sin(theta)
        return Matrix([[c, s],
                       [s, c]])

    @staticmethod
    def ry(angle: int | float) -> Matrix:
        """
        Rotation about y-axis gate.

        :param angle: Phase shift angle in radians.
        """
        theta = angle / 2
        c, s = cos(theta), sin(theta)
        return Matrix([[c, -s],
                       [s, c]])

    @staticmethod
    def rz(angle: int | float) -> Matrix:
        """
        Rotation about z-axis gate.

        :param angle: Phase shift angle in radians.
        """
        theta = angle / 2j
        return Matrix([[exp(theta), 0],
                       [0, exp(-theta)]])

    # - Two-qubit interaction gates - #

    # TODO xx, yy, zz, xy, etc.

    # - Swap gates - #

    @staticmethod
    def ss() -> Matrix:
        """Square root of swap gate."""
        return Matrix([[2, 0, 0, 0],
                       [0, 1 + 1j, 1 - 1j, 0],
                       [0, 1 - 1j, 1 + 1j, 0],
                       [0, 0, 0, 2]]) / 2

    @staticmethod
    def sims() -> Matrix:
        """Square root of imaginary swap gate."""
        return Matrix([[sqrt(2), 0, 0, 0],
                       [0, 1, 1j, 0],
                       [0, 1j, 1, 0],
                       [0, 0, 0, sqrt(2)]]) / sqrt(2)

    @staticmethod
    def sp(power: int | float) -> Matrix:
        """
        Swap gate raised to power.

        :param power: Power.
        """
        e = exp(-1j * PI * power)
        return Matrix([[2, 0, 0, 0],
                       [0, 1 + e, 1 - e, 0],
                       [0, 1 - e, 1 + e, 0],
                       [0, 0, 0, 2]]) / 2

    @staticmethod
    def cs() -> Matrix:
        """Controlled swap gate, or Fredkin gate."""
        return embed(QuantumGates.s(), 8)

    # - Others - #

    @staticmethod
    def ccx() -> Matrix:
        """Controlled controlled-not gate, or Toffoli gate."""
        return embed(QuantumGates.x(), 8)

    # TODO Add others.
