import stdio
import sys

# Get two floats, t and v, from the command line.
t = float(sys.argv[1])
v = float(sys.argv[2])

if t > 50:
    # If t is greater than 50, write on the standard output
    # "Value must be <= 50 F"
    stdio.writeln('Value of t must be <= 50 F')

elif v <= 3:
    # If v is less than 3, write on the standard output
    # "Value of v must be > 3 mph".
    stdio.writeln('Value of v must be > 3 mph')

else:
    # If the value of t and v follow the conditions,
    # Calculate the wind chill and write its value.
    w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * v ** 0.16
    stdio.writeln(w)
