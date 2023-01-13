import stdio
import stdrandom
import sys

# Get a from command line, as an int.
a = int(sys.argv[1])

# Get b from command line, as an int.
b = int(sys.argv[2])

# Set r to a random integer between a and b, obtained by calling
# stdrandom.uniformInt().
r = stdrandom.uniformInt(a, b)


# Write r.
stdio.writeln(r)
