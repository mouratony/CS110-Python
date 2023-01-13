import math
import stdio


# Entry point.
def main():
    # Initialize...

    # ...ETA to 9.135 x 10^(-4)
    ETA = 9.135e-4
    # ...RHO  to 0.5 x 10^(-6)
    RHO = 0.5e-6
    # ...T to 297
    T = 297
    # ...R to 8.31457
    R = 8.31457

    # Initialize var and n to 0.
    var = 0
    n = 0

    while not stdio.isEmpty():
        # As long as the standard input is not empty...

        # ...get the pixels from tha standard input...
        d = stdio.readFloat()

        # ... convert the pixels into meters by multiplying pixels to 0.175 x 10^(-6).
        r = d * 0.175e-6

        # ... increment var by square of r, and n by 1
        var += r ** 2
        n += 1

    # Divide var by 2n
    var = var / (2 * n)

    # Estimate k(Boltzmann's constant) as 6 * pi * var * ETA * RHO / T.
    k = 6 * math.pi * var * ETA * RHO / T

    # Estimate Na(Avogadro's constant) as R / k.
    Na = R / k

    # Write the standard output.
    stdio.writef('%e %e\n', k, Na)


if __name__ == '__main__':
    main()
