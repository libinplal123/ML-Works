import numpy as np

productivity = np.array([
    [8, 7, 8, 6, 7, 8, 9, 8, 7, 8],
    [6, 7, 6, 7, 6, 7, 8, 7, 6, 7],
    [9, 8, 9, 8, 9, 9, 8, 9, 8, 9],
    [5, 6, 5, 6, 5, 6, 6, 5, 6, 5],
    [7, 8, 7, 8, 7, 8, 7, 8, 7, 8],
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9]
])
# total hrs per employee worked
total_hrs_per_emp=np.sum(productivity,axis=1)
print(total_hrs_per_emp)
# total hrs each day
total_hrs_per_day=np.sum(productivity,axis=0)
print(total_hrs_per_day)
# average work hrs per employee
avg_hrs_per_emp=np.average(productivity,axis=1)
print(avg_hrs_per_emp)
# avg hours per day
avg_hrs_per_day=np.average(productivity,axis=0)
print(avg_hrs_per_day)
# emp index with max hours
emp_max_hrs_index=np.argmax(total_hrs_per_emp)
print(emp_max_hrs_index)
# emp index with min hours
emp_min_hrs_index=np.argmin(total_hrs_per_emp)
print(emp_min_hrs_index)
# day index with highest hrs
day_max_hrs_index=np.argmax(total_hrs_per_day)
print(day_max_hrs_index)
# emp index with hrs > 8
max_productivity_per_emp=np.max(productivity,axis=1)
print(max_productivity_per_emp)
overworked_emp_indices=np.where(max_productivity_per_emp>8)
print(overworked_emp_indices)
# most and least productive employees diff
most_least_diff = np.max(total_hrs_per_emp) - np.min(total_hrs_per_emp)
print(most_least_diff)
