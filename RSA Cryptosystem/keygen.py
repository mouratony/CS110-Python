import rsa
import stdio
import sys


# Entry point.
def main():
    # Get two integers, lo and hi, from command line.
    lo = int(sys.argv[1])
    hi = int(sys.argv[2])

    # Get public/private keys as tuple (n, e, and d), using rsa.keygen().
    n, e, d = rsa.keygen(lo, hi)

    # Write the standard output.
    stdio.writeln(str(n) + " " + str(e) + " " + str(d))


if __name__ == '__main__':
    main()
