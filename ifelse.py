name = input()
password = input()
if name == 'Mary' or 'Joe':
    if password == 'swordfish':
      print('Access Granted!')
    elif password == 'goldfish':
      print('Access Granted!')
    else:
      print('Access Denied! Wrong password')
else:
  print('Access Denied! Wrong username')