import sys

def isvowel(s):
  return True if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u' or s == 'y' else False 

def isconsonant(s):
  return not isvowel(s)
  
def commonTotal(s1, s2):
  return True if s1%s2 == 0 or s2%s1 == 0 else False

file = open(sys.argv[1])

for line in file:
  cust, prod = line.split(';')
  cust = cust.split(',')
  prod = prod.split(',')
  SS = 0
  for name, thing in zip(cust, prod):
    thing = filter(str.isalpha, thing) #get only letters
    if len(thing)%2 == 0: #Caso 1
      name = filter(isvowel, filter(str.isalpha, name))
      SS += 1.5 * len(name) if commonTotal(len(name), len(thing)) else 1.5*(1.5*len(name))
    else: #Caso 2
      name = filter(isconsonant, filter(str.isalpha, name))
      SS += len(name) if commonTotal(len(name), len(thing)) else (1.5*len(name))
  print SS