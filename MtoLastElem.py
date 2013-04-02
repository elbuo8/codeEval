import sys

file = open(sys.argv[1])

for line in file:
  cacheLine = line.strip().replace(' ', '')
  if (len(cacheLine[:-1]) >= int(cacheLine[-1])):
    print cacheLine[::-1][int(cacheLine[-1])]

    
  