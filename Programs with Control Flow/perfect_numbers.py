import stdio
import sys

# Get n(int) from command line.
n = int(sys.argv[1])

for i in range(2, n + 1):
    # For each i from [2, n]...

    # Set total(sum of divisors of i) to 0
    total = 0

    for j in range(1, (i // 2) + 1):
        # For each j from [1, i/2],...
        if i % j == 0:
            # if i is divisible by j, increment total by j.
            total += j
    if total == i:
        # If total equals i, write i(the perfect number).
        stdio.writeln(i)
