import sys

file = open(sys.argv[1])

for line in file:
  n, p1, p2 = map(int, line.split(','))
  if (n&p1 == n&p2):
    print 'true' 
  else:
    print 'false'