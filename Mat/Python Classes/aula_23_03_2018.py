# Resolva o sistema linear  7x -8y +5z =5
#                          -4x +5y -3z = -3
#                           x - y + z  =0



import numpy as np

a = np.array([[7,- 8,5],[-4,5,-3],[1,-1,1]])

b = np.array([5,-3,0])

print("Solutions: \n" , np.linalg.solve(a,b))