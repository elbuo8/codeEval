import sys

def fib(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
   return fib(n-1) + fib(n-2) 

file = open(sys.argv[1])

for line in file:
  n = int(line.strip())
  print fib(n)