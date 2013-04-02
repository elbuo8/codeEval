import sys, math

file = open(sys.argv[1])

result = 0
for line in file:
  nums = map(int, line.strip().split(' '))
  lenOfNums = len(nums)
  if(lenOfNums%2==0):
    result += nums[(lenOfNums/2) - 1]
  else:
    result += nums[int(math.floor(lenOfNums/2))]
  #if odd floor
  #else -1
print result
  