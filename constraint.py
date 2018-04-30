import calculate
from config import *


def capacity():
    """capacity constraint satisfier.
    return: capacity binary (1: fulfilled; 0: not fulfilled)
    """
    CapacityBinary = np.zeros(len(calculate.route()))
    for a in range(len(calculate.route())):
        if calculate.DemandPerRoute()[a] <= config.capacity_vector[a]:
            CapacityBinary[a] = 1
        else:
            CapacityBinary[a] = 0
    return CapacityBinary

print("capacity constraint for each route (1: Fulfilled; 0: Not Fulfilled)\n", capacity())