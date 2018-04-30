import numpy as np
import Calculate
from Config import *


def capacity():
    CapacityBinary = np.zeros(len(Calculate.route()))
    for a in range(len(Calculate.route())):
        if Calculate.DemandPerRoute()[a] <= Config.capacity_vector[a]:
            CapacityBinary[a] = 1
        else:
            CapacityBinary[a] = 0
    return CapacityBinary

print(capacity())