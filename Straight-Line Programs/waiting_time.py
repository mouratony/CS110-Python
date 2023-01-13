import math
import stdio
import sys

# Take two floats, k(average number of events per unit of time)
# and t(waiting time until next event), from the command line.
k = float(sys.argv[1])

t = float(sys.argv[2])

# Expression to calculate Pt(probability of waiting longer than t).
Pt = math.exp(-1 * k * t)

# Write the value of Pt.
stdio.writeln(Pt)
