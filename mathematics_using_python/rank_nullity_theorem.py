'''Rank nullity  theorm states that :- Rank(A)+Nullity(A)=Number of columns of A (or) dimension of (V)

'''
import numpy as np 
from scipy.linalg import null_space
A=np.array([[1,2,3],  # np.array() → to define a matrix.
        [4,5,6],
        [7,8,9]])
rank=np.linalg.matrix_rank(A) # np.linalg.matrix_rank() → to compute the rank of a matrix.
print(f"Rank of the Matris r(A)={rank}")

ns=null_space(A)  #gives the number of columns in the null space matrix

print(f"Null space of the  dimension(V) ={ns}")

nullity= ns.shape[1] # gives the count of zero column in a matrix
print(f"Null space of the matrix ns(A) ={nullity}") 
 
if rank+nullity==A.shape[1]: 
    print("Rank-nullity theorem holds.")
else:
    print("Rank-nullity theorem does not hold.")
