import sys

file = open(sys.argv[1])

for line in file:
  nums = sorted(map(float, line.strip().split(' ')))
  for num in nums:
    print '%0.3f' % num,
  print
file.close()