import numpy as np

productivity = np.array([
#emp 1  2  3  4  5  6  7  8  9  0
    [8, 7, 8, 6, 7, 8, 9, 8, 7, 8],# mon
    [6, 7, 6, 7, 6, 7, 8, 7, 6, 7],# tue
    [9, 8, 9, 8, 9, 9, 8, 9, 8, 9],# wed
    [5, 6, 5, 6, 5, 6, 6, 5, 6, 5],# thu
    [7, 8, 7, 8, 7, 8, 7, 8, 7, 8],# fri
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9] # sat
])

print(productivity[productivity<8]) # just productivity<8 gives bool values
# working hours between 5 and 7
print(productivity[(productivity>=5) & (productivity<=7)])
# first employee working hours < 8
first_emp_working_hours=productivity[:,0]
print(first_emp_working_hours[first_emp_working_hours<8])
# last two employees working hours < 7
last_two_emp_working_hrs=productivity[:,8:10]
print(last_two_emp_working_hrs[last_two_emp_working_hrs<7])
# <8=0
productivity[productivity<8]=0
print(productivity)