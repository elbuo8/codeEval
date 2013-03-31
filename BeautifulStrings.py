import sys

file = open(sys.argv[1])

for lines in file:
  letters = map(str.lower, filter(str.isalpha, lines)) #get chars
  chart = {}
  for letter in letters:
    chart[letter] = letters.count(letter)
  letters = list(set(letters))
  result = 0
  index = 26
  for letter in sorted(letters, None, None, True):
    result += chart[letter]*index
    index -= 1
    
  print result