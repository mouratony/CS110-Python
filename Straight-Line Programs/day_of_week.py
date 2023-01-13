import stdio
import sys

# Get m(month), d(day) and y(year) from command line, as integers.
m = int(sys.argv[1])

d = int(sys.argv[2])

y = int(sys.argv[3])

# The expression to calculate the day of week.
yo = y - (14 - m) // 12

xo = yo + (yo // 4) - (yo // 100) + (yo // 400)

mo = m + 12 * ((14 - m) // 12) - 2

D = (d + xo + (31 * mo) // 12) % 7

# Write D
stdio.writeln(D)
