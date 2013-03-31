import math

def isPrime(n):
  if n == 2:
    return True
  if n < 2 or n%2 == 0:
    return False
  for i in range(3, int(n/2), 2):
    if n%i == 0:
      return False
  return True
  
primes = 0
result = 0
i = 0

while(primes != 1000):
  if isPrime(i):
    result += i
    primes += 1
  i += 1
  
print result