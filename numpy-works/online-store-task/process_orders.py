import numpy as np
data=np.loadtxt("online-store-task\\online_orders.csv",delimiter=",",skiprows=1,dtype="str")
print(data)
print(data.shape)
# total no. of orders
print(np.sum(data[:,3].astype(int)))
# average unit price
print(np.average(data[:,4].astype(int)))
# revenue per order
print(data[:,3].astype(int)*data[:,4].astype(int))
# delivery days>5
print(data[data[:,6].astype(int)>5])
# returned vs non returned order count
print(np.count_nonzero(data[:,-1]=="Yes"))
print(np.count_nonzero(data[:,-1]=="No"))
# category discount
# electronics category
elec_category=data[data[:,2]=="Electronics"]
print(np.average(elec_category[:,5].astype(int)))
# clothing category
clothing_category=data[data[:,2]=="Clothing"]
print(np.average(clothing_category[:,5].astype(int)))
# home category
Home_category=data[data[:,2]=="Home"]
print(np.average(Home_category[:,5].astype(int)))
# delivery speeds
print(np.where(data[:,6].astype(int)<=3,"Fast","Normal"))