import stdio
import sys

# Gravitational constant
G = 6.674e-11

# Get m1 and m2(masses in kg of two objects)
# , and r(distance between m1 and m2) from command line, as floats.
m1 = float(sys.argv[1])

m2 = float(sys.argv[2])

r = float(sys.argv[3])

# Expression to calculate the value of F(gravitational force).
F = G * ((m1 * m2) / r ** 2)

# Write the value of F(Gravitational force).
stdio.writeln(F)
