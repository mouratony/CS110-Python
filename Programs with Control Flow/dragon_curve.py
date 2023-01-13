import stdio
import sys

# Get n(int) from command line.
n = int(sys.argv[1])

# Set the variables dragon and nograd to the string "F".
dragon = "F"

nograd = "F"

for i in range(1, n + 1):
    # For each i from [1, n], exchange(using a temporary variable temp)
    # the value of dragon with nograd...
    temp = dragon
    dragon = nograd
    # ...and the nograd gets the value of "FRF"...
    nograd = str(temp) + 'R' + str(dragon)
    # ...and dragon gets the value of "FLF".
    dragon = str(temp) + 'L' + str(dragon)

# Write the value of dragon.
stdio.writeln(dragon)
