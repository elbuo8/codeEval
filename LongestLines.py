import sys

file = open(sys.argv[1])

LL = []
n = int(file.readline())
LL.append(file.readline())

for line in file:
  if len(line) > len(LL[-1]):
    LL.append(line)

for i in range(0,2):
  print LL.pop(),

file.close()