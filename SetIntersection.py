import sys

file = open(sys.argv[1])

for line in file:
  A, B = line.split(';')
  result = ''
  for num in sorted(list(set(A.split(',')).intersection(set(B.split(','))))):
    result += num + ','
  print result[0:len(result)-1]