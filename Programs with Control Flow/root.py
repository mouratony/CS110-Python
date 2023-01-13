import stdio
import sys

# Get an integer k, a float c, and a float epsilon from command line.
k = int(sys.argv[1])

c = float(sys.argv[2])

EPSILON = float(sys.argv[3])

# set t(our guess) to c.
t = c


while abs(1 - (c / (t ** k))) > EPSILON:
    # While the |1 - c/t^(k)| is greater than epsilon...

    # ... decrement the value of t by (t^k-c)/kt^(k-1).
    t -= ((t ** k) - c) / (k * (t ** (k - 1)))

# Write the standard output.
stdio.writeln(t)
