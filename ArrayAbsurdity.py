import sys

file = open(sys.argv[1])

for line in file:
  if len(line.strip()) != 0:
    n, x = line.strip().split(';')
    x = map(int, x.split(','))
    y = [0]*int(n)
    for i in x:
      if y[i] == 0:
        y[i] += 1
      else:
        print i
        break