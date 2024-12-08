from math import *
from matrix import *


class QuantumGates(Matrix):
    # --- Pauli gates --- #

    @staticmethod
    def gate_x() -> Matrix:
        """Pauli X gate."""
        return Matrix([[0, 1],
                       [1, 0]])

    @staticmethod
    def gate_y() -> Matrix:
        """Pauli Y gate."""
        return Matrix([[0, -1j],
                       [1j, 0]])

    @staticmethod
    def gate_z() -> Matrix:
        """Pauli Z gate."""
        return Matrix([[1, 0],
                       [0, -1]])

    # --- Controlled gates --- #

    @staticmethod
    def gate_cx() -> Matrix:
        """Controlled not gate."""
        return Matrix([[1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, 0, 1],
                       [0, 0, 1, 0]])

    @staticmethod
    def gate_cy() -> Matrix:
        """Controlled Y gate."""
        return Matrix([[1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, 0, -1j],
                       [0, 0, 1j, 0]])

    @staticmethod
    def gate_cz() -> Matrix:
        """Controlled Z gate."""
        return Matrix([[1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, -1]])

    @staticmethod
    def gate_cu(operation_gate: Matrix) -> Matrix:
        """
        Controlled U gate.

        :param operation_gate: `U` gate that operates on a single qubit.
        """
        return Matrix([[1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, operation_gate[0][0], operation_gate[0][1]],
                       [0, 0, operation_gate[1][0], operation_gate[1][1]]])

    # --- Other gates --- #

    @staticmethod
    def gate_i() -> Matrix:
        """Identity gate."""
        return identity_matrix(2)

    @staticmethod
    def gate_p(angle: float) -> Matrix:
        """
        Phase gate.

        :param angle: Phase shift angle in radians.
        """
        return Matrix([[1, 0],
                       [0, exp(1j * angle)]])

    @staticmethod
    def gate_h() -> Matrix:
        """Hadamard gate."""
        return Matrix([[1 / sqrt(2), 1 / sqrt(2)],
                       [1 / sqrt(2), -1 / sqrt(2)]])

    @staticmethod
    def gate_s() -> Matrix:
        """Swap gate."""
        return Matrix([[1, 0, 0, 0],
                       [0, 0, 1, 0],
                       [0, 1, 0, 0],
                       [0, 0, 0, 1]])

    @staticmethod
    def gate_ccx() -> Matrix:
        """Toffoli gate."""
        m = identity_matrix(8)
        m[6][6], m[7][6], m[6][7], m[7][7] = 0, 1, 1, 0

        return m
