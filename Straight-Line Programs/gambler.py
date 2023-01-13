import stdio
import sys

# Get n1 and n2 as integers, and a float p from the command line.
n1 = int(sys.argv[1])

n2 = int(sys.argv[2])

p = float(sys.argv[3])

# Formula of q.
q = 1 - p

# Expression to calculate values of P1 and P2(probabilities).
P1 = (1 - ((p / q) ** n2)) / (1 - (p / q) ** (n1 + n2))

P2 = (1 - ((q / p) ** n1)) / (1 - (q / p) ** (n1 + n2))

# Write the values of P1 and P2.
stdio.write(P1)

stdio.write(' ')

stdio.writeln(P2)
