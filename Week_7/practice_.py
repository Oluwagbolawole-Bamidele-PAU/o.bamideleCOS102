#Importing Numpy
import numpy as np

# (np) allows us to access Numpy features. (np) can be changed

#Array Fundamentals
a = np.array([1, 2, 3, 4, 5,6]) #Example of a One-Dimensional Array
a[0] #(Accessing an element in a 1-D array)
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) #Example of a Two-Dimensional Array. They can be initialized from nesting an array in another array
b[1, 3] #(Accessing an element in a 2-D array)

#Array Attributes : ndim, shape, size, dtype
print(a.ndim) #The number of dimensions of an array is contained in the (ndim) attribute
print(b.shape) # The (shape) attribute show the number of (rows, colum).e.g (3, 4)
print(a.size)  # The (size) attribute show the fixed, total number of elements in array.
print(a.dtype) #Array are typically "homogeneous". The data type is recorded in the (dtype) attribute

#HOW OT CREATE A BASIC ARRAY: np.zeros(), np.ones(), np.empty(), np.arange(), np.linespace()

#ADDING, REMOVING, AND SORTING ELEMENTS: np.sort(), np.concatenate()
#Sorting an array is simple with (np.sort()). YOu can specify the axis, kind and order.
arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
print(arr)
sorted_array = np.sort(arr)
print(sorted_array)






