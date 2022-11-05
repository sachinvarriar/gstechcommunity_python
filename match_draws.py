from random import shuffle
teams = ['India', 'Australia', 'Pakistan']
teams2 = teams.copy()

shuffle(teams2)
print(teams)
print(teams2)
for i in teams:
  for j in teams2:
    if i==j:
      pass
    else:
      match = i+' vs '+j
      print(match)