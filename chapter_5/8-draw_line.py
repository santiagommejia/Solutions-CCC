# Description
# A monochrome screen is stored as a single array of bytes, allowing eight consecutive pixels to be stored in one byte. The screen has width w, where w is divisible by 8 (that is, no byte will be split across rows). The height of the screen, of course, can be derived from the length of the array and the width. Implement a function drawLine(byte[] screen, int width, int x1, int x2, int y) which draws a horizontal line from (x1, y) to (x2, y).
# The method signature should look something like this:
# drawLine(byte[] screen, int width, int x1, int x2, int y)

import math

def drawLine(screen, width, x1, x2, y):
  height = len(screen) / width
  fullByte = 0b11111111
  startByte = (y * width) + math.floor(x1 / 8)
  startBit = x1 % 8
  endByte = (y * width) + math.floor(x2 / 8)
  endBit = x2 % 8
  for byte in range(startByte, endByte + 1):
    binary = screen[byte]
    if byte == startByte:
      mask = (1 << (8 - startBit)) - 1
      screen[byte] = binary | (fullByte & mask)
    elif byte == endByte:
      mask = (1 << (8 - endBit)) - 1
      screen[byte] = binary | (fullByte & ~mask)
    else:
      mask = ((1 << 8) - 1)
      screen[byte] = binary | (fullByte & mask)
  return screen

def printScreen(screen, width):
  height = int(len(screen) / width)
  for row in range(height):
    row = screen[(row * width) : (row * width) + width]
    line = ''
    for r in row:
      binaryStr = bin(r)[2:]
      paddedStr = binaryStr.zfill(8)
      line += paddedStr
    print(line)
  return

emptyByte = 0b0
screen = [emptyByte for _ in range(20)]
width = 4
newScreen = drawLine(screen, width, 3, 23, 2)
printScreen(newScreen, width)

