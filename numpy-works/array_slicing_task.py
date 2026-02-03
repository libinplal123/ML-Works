"""   M  E  MA CS S
vipin 43 42 45 34 23
hari 23 45 45 34 37
cibin 37 38 39 40 45
"""
import numpy as np
array_marks=np.array([
    [43,42,45,34,23],
    [23,45,45,34,37],
    [37,38,39,40,45]
])
hari_marks=array_marks[1]
print(hari_marks)
hari_maths_marks=array_marks[1,0]
print(hari_maths_marks)
all_mal_marks=array_marks[:,2]
print(all_mal_marks)
all_mal_and_cs_marks=array_marks[:,2:4]
print(all_mal_and_cs_marks)
eng_and_mal_of_h_and_c = array_marks[1:3,1:3]
print(eng_and_mal_of_h_and_c)