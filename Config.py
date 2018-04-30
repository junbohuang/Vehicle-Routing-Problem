"""
Config.py file define basic parameters in the model and feed inputs. 
"""

import numpy as np

class config():

    m = 4 #num of vehicles
    n = 9 #num of customers
    distance_matrix = np.random.rand(n+1, n+1) * 10
    np.fill_diagonal(distance_matrix, 0)
    print("distance_matrix: \n",distance_matrix)
    demand_vector = np.append(0, np.random.rand(n) * 10)
    print("demand_vector: \n",demand_vector)
    capacity_vector = np.random.rand(m) * 20
    print("capacity_vector: \n",capacity_vector)
    cost_vector = np.random.rand(m) * 5
    print("cost_vector: \n", cost_vector)

