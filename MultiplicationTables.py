for i in range(1, 13):
  for num in map(lambda x: x*i, range(1, 13)):
    if i == num:
      print num,
    else:
      print ' ' * (3 - len(str(num))) + str(num),
  print
