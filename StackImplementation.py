import sys

file = open(argv[1])

for line in file:
  stack = line.strip().split(' ').reverse()
  for num in stack:
    print num
    