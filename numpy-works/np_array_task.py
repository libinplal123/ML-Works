import numpy as np
four_array=np.full((5,5),4)
one_array=np.full((3,3),1)
one_array[1,1]=100
print(one_array)
four_array[1:4,1:4] = one_array
print(four_array)