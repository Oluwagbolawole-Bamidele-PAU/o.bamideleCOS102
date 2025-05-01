# This notebook has multiple syntax and logical errors. Your task is to fix them.

# Import numpy
import numpy as np

# Check version
print(np.version)

# Create array and check type
arr_ = np.array([101, 201, 301, 401, 501]);
print(arr_)
print(type(arr_))

# Create from list, tuple
namelist = ['Angel', 'Shemi', 'Marvel', 'Linda']
agetuple = 41, 32, 21, 19
gradedict = {"CSC102": 89, "MTH 102": 77, "CHM 102": 69, "GST 102": 99}

arr_nameList = np.array(namelist)
arr_agetuple = np.array(agetuple)
arr_gradedict = np.array(gradedict.items())

print(arr_nameList)
print(arr_agetuple)
print(arr_gradedict)

# 0-Dimension example
classNum = input("How many students are in the CSC 102 class? ")
class_arr = np.array([classNum])
if class_arr == 1:
    print("There is only", classNum, "student in CSC 102 class")
else:
    print("There are", classNum, "students in CSC 102 class")

# 1-D Array
arr = np.array[1, 2, 3, 4, 5]
print(arr)

# 2-D Array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# 3-D Array
arr = np.array([[[1, 2, 3], [4, 5, 6]],
                [[1, 2, 3], [4, 5, 6]]
                [[1, 2, 3], [4, 5, 6]]])
print(arr)

# Check number of dimensions
a = np.array(42)
b = np.array([[[1, 2, 3], [4, 5, 6]],
              [[1, 2, 3], [4, 5, 6]],
              [[1, 2, 3], [4, 5, 6]]])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array(1, 2, 3, 4, 5)

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Higher dimensions with ndmin
arr = np.array([1, 2, 3, 4], ndmin=8)
print(arr)
print('number of dimensions:', arr.ndim)

# Access elements
arr = np.array([1, 2, 3, 4])
print(arr(1))

# Access 2-D
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('5th element on 2nd row:', arr[2, 4])

# Access 3-D
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 3])

# Negative indexing
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('Last element from 2nd dim:', arr[1, -6])

# Slicing arrays
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:10])
print(arr[5:])
print(arr[:1])

# Check data type
int_arr = np.array([1, 2, 3, 4])
str_arr = np.array(['apple', 'banana', 'cherry'])
print(int_arr.dtype())
print(str_arr.dtype)

# Iteration
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    for y in x:
        print(x, y)

# 3-D iteration
arr = np.array([[[1, 2, 3], [4, 5, 6]],
                [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    print(x[0][3])
    print(x[2][0])

# Joining arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.join((arr1, arr2))
print(arr)