import numpy as np
from register import *


class GroverRegister(QuantumRegister):
    def conditional_phase_shift(self):
        for state in range(1,self.n_states):
            self.qubits[state] = -1 * self.qubits[state]
        return self

    def oracle(self):
        correct_state = 128
        self.qubits[correct_state] = -1 * self.qubits[correct_state]
        return self

register = GroverRegister(8)
register.hadamar()

cycles = np.pi/4*np.sqrt(2**register.n_qubits)
print 'cycles:', cycles

for i in range(int(np.round(cycles))):
    register.oracle().hadamar().conditional_phase_shift().hadamar()

print 'measured state:', register.measure()

