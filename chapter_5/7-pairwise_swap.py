# Description
# Write a function to swap odd and even bits in an integer with as few instructions as possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).
from testing_functions import testFunction

def pairwiseSwap(num):
  rightShift = num >> 1
  leftShift = num << 1
  size = len(bin(num)[2:])
  swapper = size % 2 == 0
  mask = 1 << size
  res = 0
  while mask != 0:
    res <<= 1
    msb = (rightShift if swapper else leftShift) & mask
    res |= 1 if msb > 0 else 0
    swapper = not swapper
    mask >>= 1
  return res

testCases = [186, 8, 4, 3, 5]
expectedResults = [117, 4, 8, 3 , 10]
testFunction(testCases, expectedResults, pairwiseSwap)