import sys

file = open(sys.argv[1])

for line in file:
  result = ''
  for num in sorted(list(set(line.strip().split(',')))):
    result += num + ','
  print result[0:len(result)-1:]