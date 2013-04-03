import sys, math

file = open(sys.argv[1])

for line in file:
  result = 0
  value = line.strip()
  for num in line.strip():
    result += int(math.pow(int(num), len(line.strip())))
  if str(result) == line.strip():
    print True
  else:
    print False
file.close()