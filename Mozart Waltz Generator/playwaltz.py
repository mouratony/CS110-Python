import stdaudio
import stdio
import sys

# Read the waltz measures from standard input into
# a 1D list
waltz = stdio.readAllInts()

# Create input error messages using sys.exit():
# ...if waltz doesn't have exactly 32 measure.
if len(waltz) != 32:
    sys.exit("A waltz must contain exactly 32 measures")

for m in range(16):
    # ...if each minuet is greater than 1 and less than 176
    if not 1 <= waltz[m] <= 176:
        sys.exit("A minuet measure must be from [1, 176]")

for t in range(16, 32):
    # ...and if each trio is greater than 1 and less than 96.
    if not 1 <= waltz[t] <= 96:
        sys.exit("A trio measure must be from [1, 96]")

for m in range(16):
    # Play each of the first 16 minuet measures.
    # stdaudio.playFile(f)
    file_name = "data/M" + str(waltz[m])
    stdaudio.playFile(file_name)

for t in range(16, 32):
    # Play each of the last 16 trio measures using
    # stdaudio.playFile(f)
    file_name = "data/T" + str(waltz[t])
    stdaudio.playFile(file_name)
