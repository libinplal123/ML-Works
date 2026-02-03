import numpy as np
array=np.array([
    [33,31,27],
    [31,30,29],
    [33,32,34]
])
print(array.ndim)
print(array.size)
print(array.shape)
print(array[0])
print(array[1])

# slicing syntax-> arr[row,col]
# row slicing
print(array[0:2])
print(array[1:3])
print(array[::2])

# column slicing
print(array[:,1:3]) # : means all rows included
print(array[:,0:2])
print(array[:,1])
print(array[2,1])
print(array[1:3,1:3])