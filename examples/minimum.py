import numpy as np
import numpy.linalg as lg
import numpy.random as random
import matplotlib.pyplot as plt

from register import *


class MinimumRegister(QuantumRegister):
    def __init__(self, n_qubits, func):
        super(MinimumRegister, self).__init__(n_qubits)

        self.func = func

        random_state = random.randint(self.n_states)
        self.threshold = func(random_state)
        self.threshold_index = random_state

    def conditional_phase_shift(self):
        for state in range(1,self.n_states):
            self.qubits[state] = -1 * self.qubits[state]
        return self

    def oracle(self):
        for state in range(self.n_states):
            if self.func(state) < self.threshold:
                self.qubits[state] = -1 * self.qubits[state]
        return self

    def cycles(self):
        return np.pi / 4 * np.sqrt(2 ** self.n_qubits)

    def search(self):
        self.hadamar()
        for i in range(int(np.round(self.cycles()))):
            self.oracle().hadamar().conditional_phase_shift().hadamar()

        return self.measure()

if __name__ == '__main__':
    register = MinimumRegister(8, lambda x: (x / 128. - 1) ** 2)

    cycles = 22.5 * np.sqrt(register.n_states) + 1.4 * np.log10(register.n_states) ** 2

    print 'cycles:', int(np.round(cycles))
    iterations = 0
    total = 0

    while total < cycles:

        register.reset()
        state = register.search()
        value = register.func(state)

        if value < register.threshold:
            register.threshold = value
            register.threshold_index = state

        iterations += 1
        total += register.cycles()
        print register.threshold_index, register.threshold, value

    register.threshold_index

    state = register.threshold_index
    print 'iterations:    ', iterations
    print 'runtime:       ', total
    print 'measured state:', register.threshold_index
    print 'measured value:', register.func(state)
