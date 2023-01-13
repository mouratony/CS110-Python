import math
import stdio
import sys

# Get p(latitude) and k(longitude) in degrees from command line, as floats.
p = float(sys.argv[1])

k = float(sys.argv[2])

# Convert p(latitude) from degrees to radians.
p = math.radians(p)

# Expression to calculate x and y values (Mercator projection).
x = k

y = (math.log((1 + math.sin(p))/(1 - math.sin(p))))/2

# Write the values of x(latitude) and y(longitude).
stdio.write(x)
stdio.write(' ')
stdio.writeln(y)
