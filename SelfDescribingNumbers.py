import sys

file = open(sys.argv[1])

for line in file:
  valid = 1
  for index, num in enumerate(line.strip()):
    if line.count(str(index)) != int(num):
      valid = 0
  print valid