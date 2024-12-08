from matrix import *
from state import *


class QuantumSolver:
    def __init__(self, hamiltonian: Matrix) -> None:
        self.hamiltonian = hamiltonian

    def evolve(self, psi: QuantumState, t: float, dt: float) -> QuantumState:
        """
        Evolve the wave function over time `t`, with a time step `dt`.

        :param psi: Initial quantum state.
        :param t: Total time of evolution.
        :param dt: Time step.
        :return: Evolved quantum state.
        """
        identity = identity_matrix(self.hamiltonian.rows)
        evolved_state = identity - 1j * self.hamiltonian * dt  # Time evolution: `U = I - iHdt`.

        psi_matrix = zip_lists_to_matrix(psi.state)  # Convert to a matrix.

        steps = int(t / dt)
        for _ in range(steps):
            psi_matrix = evolved_state @ psi_matrix

        psi.state = [row[0] for row in psi_matrix]  # Extract first column.

        psi.normalize()

        return psi
