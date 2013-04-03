import sys
'''Another approach can be creating a map inside an array indexing the ones that were used
if the whole array != 0 then print NULL else print letter by letter. It will be sorted'''
file = open(sys.argv[1])

for line in file:
  alpha = set(map(chr, range(97, 123)))
  text = set([letter for letter in line.strip().replace(' ', '').lower()])
  result = sorted(list(alpha - text))
  if len(result) > 0:
    print ''.join([letter for letter in result])
  else:
    print "NULL"
    
