# Import the libraries

import numpy as np

# Create a list, That Contains Three Nested List 
a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
print(a)

# Convert list to Numpy Array
# Every element is the same type
A = np.array(a)
print(A)


# Show the numpy array dimensions
print(A.ndim)


# Show the numpy array shape
print(A.shape)



print(A.size)

# Access the element on the second row and third column
print(A[1, 2])
# Access the element on the second row and third column with different notation
print(A[1][2])


# Access the element on the first row and first column
print(A[0][0])


# Access the element on the first row and first and second columns
print(A[0][0:2])


# Access the element on the first and second rows and third column


print(A[0:2, 2])



# Create a numpy array X
X = np.array([[1, 0], [0, 1]])
print(X) 


# Create a numpy array Y

Y = np.array([[2, 1], [1, 2]]) 
print(Y)


# Add X and Y
Z = X + Y
print(Z)


# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]]) 
print(Y)

# Multiply Y with 2
Z = 2 * Y
print(Z)

# Access the element on the first row and first and second columns
print(A[0][0:2])

# Access the element on the first and second rows and third column
print(A[0:2, 2])


# Basic Operations 

# Create a numpy array X
X = np.array([[1, 0], [0, 1]]) 

print(X)

# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]]) 
print(Y)

# Add X and Y
Z = X + Y
print(Z)


# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]]) 
print(Y)

# Multiply Y with 2
Z = 2 * Y
print(Z)

# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]]) 
print(Y)


# Create a numpy array X
X = np.array([[1, 0], [0, 1]]) 
print(X)

# Multiply X with Y
Z = X * Y
print(Z)


# We can also perform matrix multiplication with the numpy arrays A and B as follows:
# First, we define matrix A and B:

# Create a matrix A
A = np.array([[0, 1, 1], [1, 0, 1]])
print(A)

# Create a matrix B
B = np.array([[1, 1], [1, 1], [-1, 1]])
print(B)


# Calculate the dot product
Z = np.dot(A,B)
print(Z)


# Calculate the sine of Z
np.sin(Z)


# Create a matrix C
C = np.array([[1,1],[2,2],[3,3]])
print(C)

# Write your code below and press Shift+Enter to execute
a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]























