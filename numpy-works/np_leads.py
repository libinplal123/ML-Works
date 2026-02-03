import numpy as np

leads = np.array([
    # s  m    t  w   th
    [12, 18, 10, 15, 5],   # facebook
    [20, 25, 22, 18, 8],   # insta
    [18, 30, 25, 22, 10],  # youtube
    [25, 28, 30, 26, 12],  # refferal
    [30, 35, 28, 32, 15],  # walkin
    [40, 45, 38, 40, 20],  # reddit
    [35, 50, 42, 45, 25]   # camp
    
])

# task1: total leads generated each day
total_leads_each_day = np.sum(leads,axis=0)
print(total_leads_each_day)
# task2: total leads from each source in 7 days
total_leads_from_each_source = np.sum(leads,axis=1)
print(total_leads_from_each_source)
# highest lead day
print(np.max(total_leads_each_day))
print(np.argmax(total_leads_each_day))
# highest leads per day
max_each_day = np.max(leads,axis=0)
print(max_each_day)
# average leads per source
avg_leads_from_each_source = np.average(leads,axis=1)
print(avg_leads_from_each_source)
# avg leads per day
avg_leads_per_day = np.average(leads,axis=0)
print(avg_leads_per_day)
# highest lead source
highest_lead_source = np.argmax(total_leads_from_each_source)
print(highest_lead_source)