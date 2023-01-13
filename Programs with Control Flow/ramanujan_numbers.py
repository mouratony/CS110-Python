import stdio
import sys

# Get n(int) from command line.
n = int(sys.argv[1])

# Write four nested while loops...
# ... Set a(1st positive integer) to 1 1
a = 1
while a ** 3 <= n:
    # While a^3 is less and equal to n,
    # set the value of b(2nd positive integer) to a + 1
    b = a + 1
    while b ** 3 <= n - a ** 3:
        # While b^3 is less and equal to n - a^3,
        # set c(3rd positive integer) to a + 1
        c = a + 1
        while c ** 3 <= n:
            # While c^3 is less and equal to n,
            # set d(4th positive integer) to c + 1
            d = c + 1
            while d ** 3 <= n - c ** 3:
                # While d^3 is less and equal to ne - c^3,
                # total equals to a^3 + b^3.
                total = a ** 3 + b ** 3
                if c ** 3 + d ** 3 == total:
                    # if c^3 + d^3 equals total...
                    first_part = str(a) + "^3 + " + str(b) + "^3"
                    second_part = str(c) + "^3 + " + str(d) + "^3"
                    # ...using the concatenation write the standard output.
                    stdio.writeln(str(total) + " = " + first_part + " = " + second_part)
                d += 1
            c += 1
        b += 1
    a += 1
# At the end of each while loop increment the value of the positives integers
# by 1.
