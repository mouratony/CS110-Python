import math
import stdio
import sys

# Get theta1(angle of incidence in degrees),
# n1(index of refraction of medium 1), and n2(index of refraction of medium 2)
# from command line, as floats.
theta1 = float(sys.argv[1])

n1 = float(sys.argv[2])

n2 = float(sys.argv[3])

# Convert theta1 from degrees to radians.
theta1 = math.radians(theta1)

# Expression to calculate theta2(angle of refraction).
expr = (n1 / n2) * math.sin(theta1)

theta2 = math.asin(expr)

# Convert theta2 from radians to degrees.
theta2 = math.degrees(theta2)

# Write the value of theta2
stdio.writeln(theta2)
