import numpy as np


A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[7, 8, 9],
              [1, 2, 3]])

print("Matrix A:\n", A)
print("\nMatrix B:\n", B)


add_result = np.add(A, B)
print("\nAddition of matrices:\n", add_result)


sub_result = np.subtract(A, B)
print("\nSubtraction of matrices:\n", sub_result)


mul_result = np.multiply(A, B)
print("\nElement-wise Multiplication:\n", mul_result)


transpose_A = np.transpose(A)
print("\nTranspose of A:\n", transpose_A)


A2 = np.array([[1, 2],
               [3, 4],
               [5, 6]])  
B2 = np.array([[7, 8, 9],
               [10, 11, 12]])  

dot_result = np.dot(A2, B2)
print("\nMatrix Multiplication (Dot Product):\n", dot_result)


C = np.array([[2, 3],
              [1, 4]])
det_C = np.linalg.det(C)
inv_C = np.linalg.inv(C)

print("\nMatrix C:\n", C)
print("Determinant of C:", det_C)
print("Inverse of C:\n", inv_C)
