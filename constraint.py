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

def demand(delivered, request):
    """customer's demand constraint satisfier."""
    DemandBinary = 0
    if delivered >= request:
        DemandBinary = 1
    else:
        DemandBinary = 0

    return DemandBinary