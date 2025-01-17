﻿import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming

distance_matrix = np.array([
    [0,30.4,23.9,28.4,24.7,14.2,25.7,14.1,21,22.6,17.2,25.3],
    [30.4,0,13.9,10.6,8.8,30.2,12.5,17.2,13,15.3,40.9,33.5],
    [23.9,13.9,0,7.3,7.9,20.1,4.6,11.1,4.6,22.8,31.3,23.6],
    [28.4,10.6,7.3,0,10.1,25,3.9,16.1,9.5,16.6,36.3,28.5],
    [24.7,8.8,7.9,10.1,0,17.5,9.1,8.5,3.7,13.8,28.8,24.8],
    [14.2,30.2,20.1,25,17.5,0,21.1,9.3,16.2,16.8,19.4,15.2],
    [25.7,12.5,4.6,3.9,9.1,21.1,0,14.8,8.3,15.4,35,27.2],
    [14.1,17.2,11.1,16.1,8.5,9.3,14.8,0,9.3,16.7,25.2,26.7],
    [21,13,4.6,9.5,3.7,16.2,8.3,9.3,0,18.3,26.9,24.3],
    [22.6,15.3,22.8,16.6,13.8,16.8,15.4,16.7,18.3,0,32,30.1],
    [17.2,40.9,31.3,36.3,28.8,19.4,35,25.2,26.9,32,0,34.8],
    [25.3,33.5,23.6,28.5,24.8,15.2,27.2,26.7,24.3,30.1,34.8,0]
])
permutation, distance = solve_tsp_dynamic_programming(distance_matrix)

tour = str(permutation[0])
for i in range(1, len(permutation)):
    tour += ' -> ' + str(permutation[i])
tour += ' -> ' + str(permutation[0])
# Print the tour in the desired format
print(tour)
print("Total distance : {} km".format(distance))


