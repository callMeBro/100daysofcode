# # create dictionary with tuple keys 
# my_dict = {('a', 'b'): 1, ('c', 'd'): 2}

# # Accessing values
# print(my_dict[('a', 'b')])  # Output: 1
# print(my_dict[('c', 'd')])  # Output: 2

# # Adding a new key-value pair
# my_dict[('e', 'f')] = 3

# # Dictionary after addition
# print(my_dict)  # Output: {('a', 'b'): 1, ('c', 'd'): 2, ('e', 'f'): 3}
##############################################################################

# import csv
# import pandas 

# # Open the CSV file in read mode
# with open('email.csv', 'r') as csvfile:
#   # Create a reader object
#   csv_reader = csv.reader(csvfile)
  
#   # Iterate through the rows in the CSV file
#   for row in csv_reader:
#     # Access each element in the row
#     print(row)


    # List of Methods to Read a CSV File in Python
    # Read CSV file using csv.reader
    # Read CSV file using .readlines() function
    # Read CSV file using Pandas
    # Read CSV file using csv.DictReader

##############################################################################

# # import numpy library
import numpy as np 

# # Create a numpy array
# a = np.array([0, 1, 2, 3, 4])
# a


# # Print each element
# print("a[0]:", a[0])
# print("a[1]:", a[1])
# print("a[2]:", a[2])
# print("a[3]:", a[3])
# print("a[4]:", a[4])


# print(np.__version__)


# # Check the type of the array
# type(a)


# # Check the type of the values stored in numpy array
# a.dtype


# b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])

# # Enter your code here

# # Create numpy array
# c = np.array([20, 1, 2, 3, 4])
# c

# # Assign the first element to 100
# c[0] = 100
# c

# # Assign the 5th element to 0
# c[4] = 0
# c

# a = np.array([10, 2, 30, 40,50])
# # Enter your code here


# # Slicing the numpy array
# d = c[1:4]
# d


# # Set the fourth element and fifth element to 300 and 400
# c[3:5] = 300, 400
# c

# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1:5:2])

# print(arr[:4])

# print(arr[4:])

# print(arr[1:5:])

################################################################################

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# even = arr[arr % 2 == 0]
print(arr[1:8:2])
# print(even)


# Create the index list
select = [0, 2, 3, 4]
select

# Use List to select elements
d = c[select]
d

# Assign the specified elements to new value
c[select] = 100000
c

# Create a numpy array
a = np.array([0, 1, 2, 3, 4])
a

# Get the size of numpy array
a.size

# Get the number of dimensions of numpy array
a.ndim

# Get the shape/size of numpy array
a.shape


##############################################################################

# Numpy Statistical Functions
# Create a numpy array
a = np.array([1, -1, 1, -1])


# Get the mean of numpy array
mean = a.mean()
mean

# Get the standard deviation of numpy array
standard_deviation=a.std()
standard_deviation

# Create a numpy array
b = np.array([-1, 2, 3, 4, 5])
b


# Get the biggest value in the numpy array
max_b = b.max()
max_b


# Get the smallest value in the numpy array
min_b = b.min()
min_b

##############################################################################
# Numpy Array Operations
u = np.array([1, 0])
u

v = np.array([0, 1])
v

##############################################################################
# Numpy Array Addition
z = np.add(u, v)
z


a = np.array([10, 20, 30])
a

b = np.array([5, 10, 15])
b

c = np.subtract(a, b)
print(c)

##############################################################################
# Numpy Array Multiplication

# Create a numpy array
x = np.array([1, 2])
x

# Create a numpy array
y = np.array([2, 1])
y

# Numpy Array Multiplication-- can multiply every element in the array by 2
z = np.multiply(x, y)
z


####################################################################################
# Consider the vector numpy array a:
z = np.multiply(x, y)
z

# Consider the vector numpy array b:
b = np.array([2, 10, 5])
b

# We can divide the two arrays and assign it to c:
c = np.divide(a, b)
c



# Perform division operation on the given numpy array arr1 and arr2:
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])
arr3 = np.divide(arr1, arr2)

####################################################################################


# Dot product 
# The dot product of the two numpy arrays u and v is given by:
X = np.array([1, 2])
Y = np.array([3, 2])

# Calculate the dot product
np.dot(X, Y)


#Elements of X
print(X[0])
print(X[1])

#Elements of Y
print(Y[0])
print(Y[1])

arr1 = np.array([3, 5])
arr2 = np.array([2, 4])

# Enter your code here
np.dot(arr1, arr2)


# Adding Constant to a Numpy Array

# Create a constant to numpy array

u = np.array([1, 2, 3, -1]) 
u

# Add the constant to array

u + 1

####################################################################################

# Mathematical Functions
# The value of pi
np.pi


# Create the numpy array in radians
x = np.array([0, np.pi/2 , np.pi])

# We can apply the function sin to the array x and assign the values to the array y;
# this applies the sine function to each element in the array:

# Calculate the sin of each elements
y = np.sin(x)
y


#######################################################################################

# Linespace
# A useful function for plotting mathematical functions is linspace. Linspace returns evenly 
# spaced numbers over a specified interval. 

#  numpy.linspace(start, stop, num = int value)

# start : start of interval range

# stop : end of interval range

# num : Number of samples to generate.

# Makeup a numpy array within [-2, 2] and 5 elements
np.linspace(-2, 2, num=5)

# Make a numpy array within [-2, 2] and 9 elements
np.linspace(-2, 2, num=9)

# Make a numpy array within [0, 2π] and 100 elements 
x = np.linspace(0, 2*np.pi, num=100)

# Calculate the sine of x list
y = np.sin(x)

# Plot the result
plt.plot(x, y)



# Consider the list [1, 2, 3, 4, 5] and [1, 0, 1, 0, 1]. Cast both lists to a numpy array then multiply them together

# Write your code below and press Shift+Enter to execute
a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 0, 1, 0, 1])
a * b

















