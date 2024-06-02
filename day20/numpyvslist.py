# Homogeneous Data: NumPy arrays are homogeneous, meaning all elements are of the same data type. This allows NumPy to allocate memory more efficiently and perform operations faster, as it doesn't need to handle type checks for each element.

# Contiguous Memory Layout: NumPy arrays are stored in contiguous blocks of memory, unlike Python lists which are arrays of pointers to objects scattered across memory. This contiguous layout improves cache efficiency and reduces memory overhead.

# Vectorized Operations: NumPy provides support for vectorized operations, which allow you to apply operations to entire arrays at once, rather than having to loop through elements individually. This leverages highly optimized C and Fortran libraries under the hood, leading to significant speed improvements.

# Optimized C/Fortran Backend: Many of NumPy's operations are implemented in C or Fortran, which are compiled languages and thus much faster than Python, an interpreted language. NumPy operations often call these underlying optimized libraries, resulting in faster execution.

# Reduced Overhead: NumPy operations have less overhead compared to operations on Python lists because NumPy bypasses many of the dynamic features of Python that introduce overhead (such as type checking, handling of dynamic typing, etc.).

# Broadcasting: NumPy supports broadcasting, which allows it to perform operations on arrays of different shapes in a highly efficient manner, avoiding the need for explicit loops and thus speeding up computation.

import numpy as np
import time

# Creating large arrays and lists
size = 1000000
numpy_array = np.arange(size)
python_list = list(range(size))

# Timing NumPy operation
start_time = time.time()
numpy_sum = np.sum(numpy_array)
numpy_duration = time.time() - start_time

# Timing Python list operation
start_time = time.time()
python_sum = sum(python_list)
python_duration = time.time() - start_time

print(f"NumPy duration: {numpy_duration:.5f} seconds")
print(f"Python list duration: {python_duration:.5f} seconds")



# Example 1: Creating an Array from Random Integers and Filling with a Constant
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
full_like_a = np.full_like(a, 7)
print(full_like_a)

# Example 2: Changing the Data Type
# Create another array with random integers
b = np.random.randint(0, 50, size=(2, 5))
print("Original array (b):")
print(b)

# Create a new array with the same shape as 'b', but filled with 3.14 and as floats
full_like_b_float = np.full_like(b, 3.14, dtype=float)
print("\nNew array filled with 3.14 (dtype=float):")
print(full_like_b_float)

# Example 3: Different Memory Layout (Fortran Order)
# Create an array with random integers
c = np.random.randint(10, 20, size=(4, 3))
print("Original array (c):")
print(c)

# Create a new array with the same shape as 'c', filled with 0, using Fortran order
full_like_c_fortran = np.full_like(c, 0, order='F')
print("\nNew array filled with 0 (Fortran order):")
print(full_like_c_fortran)


# Example 4: Using Multi-Dimensional Arrays
# Create a multi-dimensional array with random integers
d = np.random.randint(0, 10, size=(2, 3, 4))
print("Original array (d):")
print(d)

# Create a new array with the same shape as 'd', filled with -1
full_like_d = np.full_like(d, -1)
print("\nNew array filled with -1:")
print(full_like_d)


# Example 5: Specifying Shape
# Create an array with random integers
e = np.random.randint(0, 100, size=(3, 3))
print("Original array (e):")
print(e)

# Create a new array with a different shape than 'e', filled with the value 5
full_like_e_different_shape = np.full_like(e, 5, shape=(2, 2))
print("\nNew array with different shape filled with 5:")
print(full_like_e_different_shape)


# Example 6: Vector Addition with Random Integers python
# Create two vectors with random integers
vec1 = np.random.randint(0, 100, size=5)
vec2 = np.random.randint(0, 100, size=5)
print("Vector 1 (random integers):")
print(vec1)
print("Vector 2 (random integers):")
print(vec2)

# Perform vector addition
vec_sum = vec1 + vec2
print("\nSum of vectors:")
print(vec_sum)

# Example 7: Vector Addition with Random Decimal Numbers
# Create two vectors with random decimal numbers
vec1 = np.random.rand(5)
vec2 = np.random.rand(5)
print("Vector 1 (random decimals):")
print(vec1)
print("Vector 2 (random decimals):")
print(vec2)

# Perform vector addition
vec_sum = vec1 + vec2
print("\nSum of vectors:")
print(vec_sum)


# Example 8: Vector Addition with Identity Matrix Diagonals
# Create an identity matrix
identity_matrix = np.eye(5)
print("Identity matrix:")
print(identity_matrix)

# Extract the diagonal elements to form a vector
vec1 = np.diag(identity_matrix)
print("\nVector from identity matrix diagonal (vec1):")
print(vec1)

# Create another vector with random integers
vec2 = np.random.randint(0, 10, size=5)
print("Vector 2 (random integers):")
print(vec2)

# Perform vector addition
vec_sum = vec1 + vec2
print("\nSum of vectors:")
print(vec_sum)

# Example 9: Using numpy.full_like to Create Vectors and Perform Addition
# Create a vector with random integers
vec = np.random.randint(0, 50, size=5)
print("Original vector (random integers):")
print(vec)

# Create a new vector with the same shape and type as 'vec', filled with the value 3
full_like_vec = np.full_like(vec, 3)
print("\nVector filled with 3:")
print(full_like_vec)

# Perform vector addition
vec_sum = vec + full_like_vec
print("\nSum of original vector and vector filled with 3:")
print(vec_sum)