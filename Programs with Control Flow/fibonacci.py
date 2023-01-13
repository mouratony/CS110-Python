import stdio
import sys

# Get n(int) from command line.
n = int(sys.argv[1])

# Set a, b (the first two Fibonacci numbers) to 1, and it to 3.
a = 1
b = 1
i = 3

while i <= n:
    # While i is less and equal to n, exchange(using temporary variable)
    # a and b...
    temp = a
    a = b

    # ...but b is equal to the sum of a(which is assigned to temp)
    # and b(which is assigned to a)...
    b = temp + a

    # ... and increment i by 1.
    i += 1

#  Write b (nth Fibonacci number).
stdio.writeln(b)
