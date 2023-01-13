import stdio
import sys

# Get two integers, n and k, from the command line.
n = int(sys.argv[1])

k = int(sys.argv[2])

# Set total to 0.
total = 0
for i in range(1, n + 1):
    # For each i from [1, n], increment total by i^k
    total += i ** k
# Write total (sum of powers).
stdio.writeln(total)
