import numpy as np
from quop_mpi.algorithms import ansatz
from mpi4py import MPI
from quop_mpi.unitaries import diagonal, sparse
from quop_mpi.states import equal
from quop_mpi.operators import diagonal_uniform, sparse_hypercube
from quop_mpi.params import uniform

COMM = MPI.COMM_WORLD

qubits = 4
system_size = 2**qubits

U1 = diagonal(diagonal_uniform, parameter_function = uniform)
U2 = sparse(sparse_hypercube, parameter_function = uniform)

qaoa = ansatz(system_size, COMM)
qaoa.set_unitaries([U1, U2], 0)
qaoa.set_depth(1)
x = qaoa.get_initial_params()
qaoa.evolve_state(x)
print(np.abs(qaoa.final_state)**2)