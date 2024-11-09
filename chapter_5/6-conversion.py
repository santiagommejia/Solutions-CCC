# Description
# Write a function to determine the number of bits you would need to flip to convert integer A to integer B.
# EXAMPLE
# Input: 29 (or: 11101), 15 (or: 01111)
# Output: 2

from testing_functions import testFunction

def conversion(a, b):
  maxn = max(a, b)
  minn = min(a, b)
  count = 0
  while maxn != 0:
    count += (maxn & 1) ^ (minn & 1)
    maxn >>= 1
    minn >>= 1
  return count 

def test(args):
  return conversion(args[0], args[1])

testCases = [[29, 15], [743, 747], [11, 13], [8, 7], [5, 6], [743, 727], [743, 745], [8, 1]]
expectedResults = [2, 2, 2, 4, 2, 2, 3, 2]
testFunction(testCases, expectedResults, test)
