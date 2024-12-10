# QuantumTautology: A Quantum Computer Emulator

*December 7, 2024*
___
This project aims at creating a quantum computer simulator. We want to write a program that numerically evaluates wave functions over time and emulates quantum operations (gates) on these states in order to run quantum algorithms. Our approach to achieve time-evolving states will be to consider some “time-advancing” gate that will change the state of the wave function, for some period of time, using a specified Hamiltonian
___

## TODOs

### Part I: Initialization and Basic Solver
* [ ] **Initialize Quantum States**
  * Create a class to represent the wave function.
  * Implement methods to initialize a simple 1D wave function for a particle in a potential well.

* [ ] **Numerical Solver for Time Evolution**
  * Develop a solver for Schrödinger’s equation.
  * Verify that a particle in a stationary state remains constant over time.

### Part II: Quantum Gates and Algorithms
* [x] **Matrix Class for Quantum Gates**
  * Implement matrix representations for basic quantum logic gates (e.g., Hadamard, Pauli-X, Pauli-Y, Pauli-Z, CNOT).

* [ ] **Apply Quantum Gates**
  * Develop methods to apply these gates to the quantum states.
  * Test the gates individually to ensure correct state transformations.

* [ ] **Entanglement and Superposition**
  * Create and manipulate entangled states.
  * Implement superposition states and verify their properties through simulation.

* [ ] **Quantum Algorithms**
  * Implement simple quantum algorithms (e.g., Grover’s search, Shor’s algorithm).
  * Verify the outputs by comparing with expected results.

### Part III: Visualization
* [ ] **Wave Function Visualization**
  * Develop visualization tools to plot the wave function.
  * Implement animations to show the evolution of the wave function over time.

* [ ] **Quantum Circuit Visualization**
  * Create visual representations of quantum circuits.
  * Illustrate the process of quantum algorithms through step-by-step visualizations.

### Additional Features (Optional)
* [x] **Advanced Quantum Gates**
  * Implement additional quantum gates.

* [ ] **User Interface**
  * Develop a simple GUI to interact with the quantum simulator.



## Development

The first steps in this project will pertain to the implementation of a numerical solver and initialization of quantum states. That is, we will create a program to solve Schrödinger’s equation to compute the evolution over time of the wave function and also a program to store and treat the information of the wave function (one-dimensional).
	
The following developments will deal with the implementation of quantum gates, which will influence the current wave function. These gates will change the states immediately (no time evolution). We will also incorporate the superposition and entanglement quantum states.

### Part I
In the first part, we will initialize a simple one-dimensional wave function for a particle in a potential well. We will then verify — using our solver of the quantum state over time — that a particle in a stationary state remains constant (unchanged).
	
### Part II
In this part, we will try our gate implementations: first, by creating an entangled system and computing its evolution, and then by performing some quantum algorithms and comparing the outputs with the corresponding known results to verify the correctness of our program.
	
### Part III
If time permits, the implementation of some visualization of the wave function over its journey through a quantum circuit (algorithm) might be helpful.

## Links
* [Quantum logic gates](https://en.wikipedia.org/wiki/Quantum_logic_gate)
* [List of quantum logic gates](https://en.wikipedia.org/wiki/List_of_quantum_logic_gates)
* [Quantum algorithms](https://en.wikipedia.org/wiki/Quantum_algorithm)