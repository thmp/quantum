from register import *
from memory import *

register = QuantumRegister(3)

register.set_qubit(1, 1./np.sqrt(2), 1./np.sqrt(2))
register.set_qubit(2, 1./np.sqrt(3), np.sqrt(2./3.))

register.hadamar(qubits=[1,0,0])
register.cswap(0,1,2)
register.hadamar(qubits=[1,0,0])

def avg(values):
    return sum(values)/float(len(values))

eps = 1e-4
average = avg([register.measure() < 4 for i in range (int(eps**(-1)))])

print "Measure avg", np.sqrt(average*2-1)
print "Probability", register.probability([0,None,None])
print "Correct    ", 1./np.sqrt(2)*1./np.sqrt(3) + 1./np.sqrt(2)*np.sqrt(2./3.)