import stdio
import stdrandom
import sys

# Take n(number of sides of a fair dice) from command line, as an integer.
n = int(sys.argv[1])

# Expressions of two numbers rolled.
first_roll = stdrandom.uniformInt(1, n)

second_roll = stdrandom.uniformInt(1, n)

# Write the sum of the numbers rolled.
stdio.writeln(first_roll + second_roll)
