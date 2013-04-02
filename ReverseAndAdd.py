import sys

file = open(sys.argv[1])

for line in file:
  num = line.strip()
  iterations = 0
  while True:
    iterations += 1
    num = str(int(num) + int(num[::-1]))
    if(num == num[::-1]):
      print iterations, num 
      break
    