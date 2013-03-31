import sys

file = open(sys.argv[1])

for line in file:
  x, n = map(int, line.split(','))
  i = 1
  while True:
    if i*n >= x:
      print i*n
      break
    i += 1
    