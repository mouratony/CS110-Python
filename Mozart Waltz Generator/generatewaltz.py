import stdarray
import stdrandom
import stdio

# Get the minuets from the standard input and create a 2D array.
# This is the table of minuets.
minuet = stdarray.create2D(11, 16, 0.0)
for i in range(11):
    for j in range(16):
        minuet[i][j] = stdio.readInt()

# Get the trios from the standard input and create a 2D array.
# This is the table of trios.
trio = stdarray.create2D(6, 16, 0.0)
for i in range(6):
    for j in range(16):
        trio[i][j] = stdio.readInt()

for i in range(16):
    # For each column of the table of minuet with a sequence of 16...
    # ...roll two dice and sum their value in order to
    # obtain the row index which is in the interval of [0,10]...
    d1 = stdrandom.uniformInt(0, 6)
    d2 = stdrandom.uniformInt(0, 6)
    totald = d1 + d2
    # ...then write the standard output (a random sequence of 16 minuet measures).
    n = minuet[totald][i]
    stdio.write(str(n) + ' ')

for i in range(16):
    # For each column of the table of trio with a sequence of 16...
    # ...roll a die to obtain the row index which is a value from [0,5]...
    d1 = stdrandom.uniformInt(0, 6)
    # ...then write the standard output (a random sequence of 16 trio measures).
    n = trio[d1][i]
    stdio.write(str(n) + ' ')

# Newline.
stdio.writeln()
