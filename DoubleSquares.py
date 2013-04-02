import sys, math

file = open(sys.argv[1])

file.readline() #pichea la primera

for line in file:
  x = int(line.strip())
  possibleValues = range(int(math.floor(math.sqrt(x))), -1, -1)
  counter = 0
  for i in possibleValues:
    y = math.sqrt(x - i*i)
    z = int(y)
    if (z == y and z in possibleValues):
      #print i, z
      possibleValues.remove(z)
      counter += 1
  print counter
file.close()