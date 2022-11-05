print("Enter length of sequence")
n=int(input())
n1, n2 = 0, 1
i = 0
print(n1)
print(n2)
while i<n-2:
  nth = n1 + n2
  # update values
  n1 = n2
  n2 = nth
  i += 1
  print(nth)