import stdio
import sys

# Take three integers, x, y, and z from command line.
x = int(sys.argv[1])

y = int(sys.argv[2])

z = int(sys.argv[3])

# Get the smallest value(m), the biggest value(M), and the middle value(n).
m = min(x, y, z)

M = max(x, y, z)

# The arithmetic combination of x, y , z , m , and M
# to get the value of n (middle value).
#
n = x + y + z - m - M

# Write the numbers in ascending order.
stdio.write(m)
stdio.write(' ')
stdio.write(n)
stdio.write(' ')
stdio.writeln(M)
