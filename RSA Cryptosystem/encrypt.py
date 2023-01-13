import rsa
import stdio
import sys


# Entry point.
def main():
    # Get two integers, n and e, from command line.
    n, e = int(sys.argv[1]), int(sys.argv[2])

    # set width to the number of bits needed to encode n (using rsa.bitLength())
    width = rsa.bitLength(n)

    # Get a message from standard input
    message = stdio.readAll()

    for c in message:
        # For each character in message...

        # ...turn c into an integer.
        x = ord(c)

        # ...encrypt x using rsa.encrypt().
        encrypted = rsa.encrypt(x, n, e)

        # ...and write the standard output.
        stdio.write(str(rsa.dec2bin(encrypted, width)))
    stdio.writeln()


if __name__ == '__main__':
    main()
