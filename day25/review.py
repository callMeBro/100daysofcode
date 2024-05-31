import numpy as np

# # create a numpy array
# a = np.array([1, 2, 3])


# # list in python 
# lista = [1, 2, 3]

# # convert list into numpy array
# convertedlist = np.array(lista)

# # show the numpy array size
# converted_numpysize = convertedlist.size


# # craete array with boolean ints and fill with a constant 


# # create an array with boolean values
# # boolean_array= np.array([True, False, True], dtype=bool)
# # print(boolean_array)

# # #np array of int values
# # int_values = np.array([1, 2, 3], dtype=int)
# # print(int_values)

# # # add integer values
# # combined_array = np.concatenate((boolean_array, int_values))
# # print(combined_array)

# # # combine boolean and int array
# # constant_value = 1
# # final_array = np.full((10,), constant_value)  # Creating an array of size 10 filled with 0



# # final_array[:len(combined_array)] creates a slice of final array that includes element from the start of the final_array
# # This assigns the values of combined_array to the corresponding positions in the slice of final_array
# # final_array[:len(combined_array)] = combined_array  # Replacing first part with the combined array

# # print(final_array)


# # generate a random integer 
# # random_c = np.random.randint(0, 100, size=None, dtype=int)                #none means a simple integer is generated
# # random_d= np.random.randint(0, 100, size=None, dtype=int)



# # fill with a constant value

# # create an array with boolean values and fill with a constant 
# # boolean_int_array= np.array([True, False, True], dtype=bool)
# # print(boolean_int_array)
# a_size = 100
# constant_value = 1
# boolean_int_array = np.full(a_size, constant_value, dtype=bool)
# print(boolean_int_array)



# # vector addition with random ints:: Note vector addition has to be done with an numpy arraylist 
# vector1 = np.array([1,2,3,4,5])
# vector2 = np.array([1,2,3,4,5])
# sum = vector1 + vector2
# print(sum)

# # print(random_d)



# # create a list
# # list_a = [0,1,2,3,4,5,6,7,8,9]
# # convet a list to a numpy array
# # numpy_a = np.array(list_a)

# # print(numpy_a)


# #access the element on the firat row second column 
# numpy_b = np.array([[1,2,3], [1,2,3]])
# print(numpy_b)
# first_second = numpy_b[0, 1]
# print(first_second)


# # create numpy array list y and z 
# Y = np.array([[1,2,3], [1,2,3], [1,2,3]]) 
# Z = np.array([[1,2,3], [1,2,3], [1,2,3]])

# print("Numpy arrays Y and Z")
# print(Y)
# print(Z)

# # add the np arrays
# sum = Y + Z 
# print("sum")
# print(sum)

# # find the dot product of numpy array Z & Y 
# #access the element on the firat row second column 
# numpy_b = np.array([[1,2,3], [1,2,3]])
# print(numpy_b)
# first_second = numpy_b[0:1]

# product = np.dot(Z, Y)
# print("Product")
# print(product)

vec_ints = np.random.randint(101, size=10)
# create a vector wih random ints 
vector_a = np.copy(vec_ints)              #copy ensures that vector_a gets its own copy of the data

# print(vector_a)


file_a = "words.txt"
# open up a file in read mode 
with open(file_a, "r+") as f:
    data = f.read()
    print("file read")
    
    
# create numpy array
a = np.array([1, 2, 3, 4, 5, 6, 7])

# set forth and fifth element of a numpy array to zero 
forth_e = a[3]
fifth_e = a[4]

print(forth_e)
print(fifth_e)

# get size of numpy array
a.size

# create a list that contains three nest list of numpy arrays
list_a= [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]

print(list_a)






