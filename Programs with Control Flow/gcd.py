import stdio
import sys

# Get two integers, p and q, as command line arguments.
p = int(sys.argv[1])

q = int(sys.argv[2])

while p % q != 0:
    # While the remainder of p and q is not 0, exchange(using a temporary variable temp)
    # p and q...
    temp = p
    p = q
    # ...but q gets the value of the remainder p(which is assigned to temp)
    # and q(which is assigned to p)
    q = temp % p

# Write the value of q(the greatest common divisor).
stdio.writeln(q)
