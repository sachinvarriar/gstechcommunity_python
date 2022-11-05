x=[[1,2],[3,4]]
y=[[4,5],[6,9]]
print(x)
print(y)
for i in range(len(x)):
  for j in range(len(x)):
    print(x[i][j]*y[i][j])