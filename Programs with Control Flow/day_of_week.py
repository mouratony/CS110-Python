import stdio
import sys

# Get m(month), d(day), and y(year) as integers from the command line.
m = int(sys.argv[1])

d = int(sys.argv[2])

y = int(sys.argv[3])

# The equations to calculate the day of week(D).
yo = y - (14 - m) // 12

xo = yo + (yo // 4) - (yo // 100) + (yo // 400)

mo = m + (12 * ((14 - m) // 12)) - 2

D = (d + xo + ((31 * mo) // 12)) % 7

# The if statement to write the output based on D.
if D == 0:
    stdio.writeln("Sunday")
elif D == 1:
    stdio.writeln("Monday")
elif D == 2:
    stdio.writeln("Tuesday")
elif D == 3:
    stdio.writeln("Wednesday")
elif D == 4:
    stdio.writeln("Thursday")
elif D == 5:
    stdio.writeln("Friday")
elif D == 6:
    stdio.writeln("Saturday")
