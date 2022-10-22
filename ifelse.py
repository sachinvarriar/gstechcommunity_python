name = input()
password = input()
if name == 'Mary':
    if password == 'swordfish':
      print('Access Granted!')
    else:
      print('Access Denied! Wrong password')
else:
  print('Access Denied! Wrong username')