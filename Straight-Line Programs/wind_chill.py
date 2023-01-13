import stdio
import sys

# Get t(temperature in fahrenheit) and v(wind speed in mph)
# from command line as floats.
t = float(sys.argv[1])

v = float(sys.argv[2])

# The expression to calculate the value of w(wind chill).
w = 35.74 + 0.6215 * t + ((0.4275 * t) - 35.75) * (v ** 0.16)

# Write the value of w(wind chill).
stdio.writeln(w)
