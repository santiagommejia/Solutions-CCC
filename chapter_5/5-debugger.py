# Description
# Explain what the following code does: ((n & (n - 1)) == 0).

# Response
# It checks if n is a power of 2 for any natural number.

for i in range(1, 33):
  print(f"{i} is a power of two: {(i & (i-1) == 0)}")

