# Description
# Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double, print the binary representation. If the number cannot be represented accurately in binary with at most 32 characters, print "ERROR".

import random
from testing_functions import testFunction

def decimalToBinaryString(n):
  finished = False
  string = ''
  while n != 0 and not finished and len(string) <= 32:
    n *= 2
    if n >= 1:
      string += '1'
      n -= 1
    else:
      string += '0'
    if n == 0:
      finished = True
  return string if finished else 'ERROR'

# for i in range(20):
#   decimalNumber = round(random.random(), 2)
#   binaryString = decimalToBinaryString(decimalNumber)
#   print(f"decimalNumber {decimalNumber} has binary: {'0.' + binaryString if binaryString != 'ERROR' else binaryString}")

testCases = [0.78, 0.75, 0.59, 0.67, 0.5, 0.42, 1.0, 0.125, 0.25]
expectedResults = ['ERROR', '11', 'ERROR', 'ERROR', '1', 'ERROR', 'ERROR', '001', '01']
testFunction(testCases, expectedResults, decimalToBinaryString)






