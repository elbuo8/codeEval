import math

def isPrime(n):
  for i in range(2, int(math.sqrt(n))):
    if n%i == 0:
      return False
  return True

for i in range(1000, 0, -1):
  if int(str(i)[::-1]) == i and isPrime(i):
    print i,
    break