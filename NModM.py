import sys, math

file = open(sys.argv[1])

for line in file:
  n, m = line.strip().split(',')
  n = int(n)
  m = int(m)
  print int(n - math.floor(n/m)*m)