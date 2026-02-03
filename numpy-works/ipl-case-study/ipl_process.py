import numpy as np
data=np.genfromtxt("ipl-case-study\\ipl_case_study.csv",delimiter=",",skip_header=1,filling_values=0,dtype="str")
# total matches
total_matches=np.count_nonzero(data[:,0])
print(total_matches)
# 2023 matches
matches_2023=data[data[:,1]=="2023"]
print(matches_2023)
# maximum and minimum runs scored by team_1
team1_runs=data[:,5].astype("int")
print(np.max(team1_runs))
print(np.min(team1_runs))
# average man_of_match_runs
print(np.average(data[:,-2].astype("int")))
# Wankhede matches
print(np.count_nonzero(data[:,4]=="Wankhede"))
# wickets>15
print(data[data[:,-1].astype("int")>15])
# team_1_runs > team_2_runs
print(data[data[:,5].astype("int")>data[:,6].astype("int")])
# total runs per match
print(data[:,5].astype("int")+data[:,6].astype("int"))
# avg total runs per match
print((data[:,5].astype("int")+data[:,6].astype("int"))/2)
# csk wins
print(np.count_nonzero(data[:,-3]=="CSK"))
# rcb matches
print(data[(data[:,2]=="RCB") | (data[:,3]=="RCB")])
# season with highest match count
seasons,match_count=np.unique(data[:,1],return_counts=True)
max_match_count_index=np.argmax(match_count)
print(seasons[max_match_count_index])
# man_of_match_runs >= 75
print(data[data[:,-2].astype("int")>=75])
# MI win percent
MI_win_percent=np.count_nonzero(data[:,-3]=="MI")/total_matches
print(MI_win_percent)
# MI vs CSK
print(data[((data[:,2]=="MI") & (data[:,3]=="CSK")) | ((data[:,2]=="CSK") & (data[:,3]=="MI")) ])
# highest scoring matches
desc_sort=data[np.argsort(data[:,5].astype("int")+data[:,6].astype("int"))][::-1]
print(desc_sort[:5])
# avg wickets per season
seasons = data[:,1]
unq_seasons=np.unique(seasons)
print(unq_seasons)
wickets=data[:,-1].astype("int")
print(wickets)
for season in unq_seasons:
    print(np.mean(wickets[seasons==season]))
# most common venue
venue, venue_count = np.unique(data[:,4],return_counts=True)
print(venue, venue_count)
max_count_venue_index=np.argmax(venue_count)
most_common_venue = venue[max_count_venue_index]
print(most_common_venue)
# team with max wins
team,win_count=np.unique(data[:,-3],return_counts=True)
print(team,win_count)
max_wins_team_index=np.argmax(win_count)
most_wins_team=team[max_wins_team_index]
print(most_wins_team)
# sorts by man of match
man_of_match_sorted=data[np.argsort(data[:,-2].astype("int"))]
print(man_of_match_sorted)