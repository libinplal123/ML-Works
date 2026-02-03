"""
1 2 3
4 5 6
7 8 9
"""
import numpy as np
two_dimensional_array=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(two_dimensional_array)
print(two_dimensional_array.ndim)
# size - total no. of elements
print(two_dimensional_array.size)
# shape - returns no. of rows and columns
print(two_dimensional_array.shape)