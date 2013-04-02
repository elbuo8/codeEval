import sys

file = open(sys.argv[1])

for line in file:
  x, s = line.strip().split(',')
  print x.find(s)