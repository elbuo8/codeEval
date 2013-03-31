import sys

file = open(sys.argv[1])

for lines in file:
  words = [word.strip() for word in lines.split(' ')]
  words.reverse()
  print ' '.join(words)