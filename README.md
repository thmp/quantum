# Quantum Algorithms for Machine Learning

Quantum computing simulation in python

## Introduction

Quantum computing was first developed as a way to efficiently simulate quantum systems, which
is not possible using classical computation devices. In 1982, Richard Feynman proposed a universal
quantum simulator, which would be able to execute these simulations without experiencing the
exponential slowdown of quantum simulations on classical computers. Since this universal
quantum simulator was a complete Turing machine, it became known as a quantum computer.

The topic reached major attention when the first algorithms for quantum computers were developed,
which were superior to their classical counterparts. It expanded the quantum computer’s
possible usages beyond the simulation of quantum systems. Important algorithms were Shor’s
algorithm for number factorization with an exponential speed-up as well as Grover’s search
algorithm showing a quadratic speedup.

Along with theoretical developments, first experimental realization of quantum computers with a
few qubits were demonstrated. In 1998, the first experimental realizations of quantum computers
with two and three qubits were presented, solving Deutsch’s algorithm as well as the Grover
search. Both employed nuclear magnetic resonance to realize the qubits. Recently, the first
industry-class quantum annealing computers were presented by D-Wave Systems.

### Simulating quantum computing

Quantum computers are not readily available yet, but quantum computing using registers of only a
few quantum bits has been verified experimentally. Commercially available quantum computing
solutions such as D-Wave’s quantum processor only provide a small set of possible instructions
available on a fully-fledged quantum computer. D-Wave’s quantum computer currently only
provides access to a quantum annealing algorithm.

To study quantum computing and its possible applications for machine learning and optimization,
we have to evaluate quantum algorithms theoretically or simulate them on classical computers.
While the simulation does not scale very well to a large number of qubits. It does provide an
insight into the workings of quantum computers on a small scale.

Here, a simulation algorithm was designed and implemented, enabling quantum computing
simulations in a python computing environment. The algorithms discussed in later chapters
were simulated using the basic quantum computing simulation functionalities discussed below.

## Project structure

In `register.py`, the basic structure of the quantum computer, a quantum register, is implemented. It
provides basic functionality to set qubits and trigger quantum gate calculations. A basic example
of a quantum memory is provided in `minimum.py` implementing QRam.

The `examples` folder contains sample implementations of a dot product calculation (`dotproduct.py`), the 
Grover algorithm (`grover.py`) and an application of the Grover algorithm to minimum finding (`minimum.py`).

Some annotated code and results can be found in the [IPython Notebook](http://nbviewer.ipython.org/github/thmp/quantum/blob/master/examples/notebook.ipynb)
