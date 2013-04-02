import sys

file = open(sys.argv[1])

counter = 0
for line in file:
  counter += int(line.strip())
print counter