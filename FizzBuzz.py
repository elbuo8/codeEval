import sys

file = open(sys.argv[1])

for lines in file:
  A, B, N = map(int, lines.split(' '))
  for i in range(1, int(N) + 1):
    if (i%(A*B)) == 0:
      print 'FB',
    elif (i%A == 0):
      print 'F',
    elif (i%B == 0):
      print 'B',
    else:
      print i,
  print ''