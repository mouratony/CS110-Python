import math
import stdio
import sys

# Get x1, y1, x2, and y2(latitude and longitude of two points on Earth)
# in degrees from the command line, as floats.
x1 = float(sys.argv[1])

y1 = float(sys.argv[2])

x2 = float(sys.argv[3])

y2 = float(sys.argv[4])

# Convert all x1, y1, x2, and y2 fromm degrees to radians.
x1 = math.radians(x1)

y1 = math.radians(y1)

x2 = math.radians(x2)

y2 = math.radians(y2)

# Expressions to calculate the value of great-circle distance d.
the_sin_part = math.sin(x1) * math.sin(x2)

the_cos_part = math.cos(x1) * math.cos(x2) * math.cos(y1 - y2)

d1 = math.acos(the_sin_part + the_cos_part)

# Convert d1 from radians into degrees to calculate d.
d1 = math.degrees(d1)

d = 111 * d1

# Write the value of d(great-circle distance).
stdio.writeln(d)
