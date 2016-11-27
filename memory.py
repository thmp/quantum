import numpy as np


class QRam(object):
    def __init__(self, accessQubits, dataQubits): 
        self.accessQubits = accessQubits
        self.dataQubits = dataQubits

        self.accessStates = 2 ** accessQubits
        self.dataStates = 2 ** dataQubits
        
        self.memory = np.zeros((self.accessStates, self.dataStates), dtype=complex)

    def retrieve(self, access): 
        out = np.zeros((self.dataStates,), dtype=complex)
        for i in range(access.shape[0]):
            out += access[i] ** 2 * self.memory[i, :]
        return out

    def store(self, access, data):
        assert access < self.accessStates
        self.memory[access,:] = data
