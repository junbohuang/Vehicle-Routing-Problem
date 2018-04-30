import numpy as np
from Config import *

"""
m = 4 #num of vehicles
n = 9 #num of customers
"""

def route():
    return np.asarray([[0, 1, 2, 3, 0],
                        [0, 4, 5, 6, 0],
                        [0, 7, 8, 9, 0],
                        [0, 0, 0, 0, 0]])

def distance():
    routes = route()
    # a: number of routes
    # b: number of customers in one route
    # length of each route may vary, thus 0 is used to fill empty customer up
    a,b = routes.shape
    distance_matrix = np.zeros((a,b))
    for i in range(a):
        for j in range(b-1):
            distance_matrix[i][j] = Config.distance_matrix[routes[i][j], routes[i][j+1]]
    return distance_matrix


def CostPerRoute():
    route_distance = [np.sum(distance()[a]) for a in range(len(distance()))]
    return route_distance * Config.cost_vector


def demand():
    routes = route()
    # a: number of routes
    # b: number of customers in one route
    # length of each route may vary, thus 0 is used to fill empty customer up
    a,b = routes.shape
    demand_matrix = np.zeros((a,b))
    for i in range(a):
        for j in range(b-1):
            demand_matrix[i][j] = Config.demand_vector[route()[i][j]]
    return demand_matrix


def DemandPerRoute():
    #DemandPerRoute = np.zeros((len(route())))
    #DemandPerRoute = [Config.demand_vector[a] for a in range(len(route()))]
    DemandPerRoute = [np.sum(demand()[a]) for a in range(len(demand()))]
    return DemandPerRoute

## check cost function
#print("cost_vector: \n", Config.cost_vector, Config.cost_vector.shape)
#print("route: \n",route(), route().shape)
#print("cost per route:\n",cost())

## check demand function
#print(Config.demand_vector)
#print(DemandPerRoute())