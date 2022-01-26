import numpy as np
from scipy import linalg
A = np.array([[2,-1,0,0],[-1,-2,-1,0],[0,-1,2,-1],[0,0,-1,2]])
P,L,U = linalg.lu(A)
print(P)
print(L)
print(U)
print(L@U)
print(LA.det(L) * LA.det(U))
print(LA.det(A))