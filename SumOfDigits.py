import sys

file = open(sys.argv[1])

for line in file:
  print sum(map(int, line.strip()))