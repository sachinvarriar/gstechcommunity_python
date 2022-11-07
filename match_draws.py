from random import shuffle
teams = ['India', 'Australia', 'Pakistan', 'WI', 'Sri Lanka','New Zealand', 'Netherlands', 'Scotland', 'England', 'Ireland', 'Bangladesh']
teams2 = teams.copy()
k=0
shuffle(teams2)
print(teams)
print(teams2)
for i in teams:
  for j in teams2:
    if i==j:
      pass
    else:
      match = i+' vs '+j
      k+=1
      print(match,k)