import rsa
import stdio
import sys


# Entry point.
def main():
    # Get two integers, n and d, from command line.
    n, d = int(sys.argv[1]), int(sys.argv[2])

    # Set width to the number of bits per character of n.
    width = rsa.bitLength(n)

    # Get the message from standard input.
    message = stdio.readAll()

    for i in range(0, len(message) - 1, width):
        # For each i in [0,len(message)-1] and increments by width...

        # ...set s to substring of message from i to i + width.
        s = message[i:i + width]

        # ...set y to decimal representation of the binary of s.(using rsa.bin2dec())
        y = rsa.bin2dec(s)

        # ... decrypt y using rsa.decrypt()
        decrypted = rsa.decrypt(y, n, d)
        # ...write the character of the decrypted value using chr().
        stdio.write(chr(decrypted))


if __name__ == '__main__':
    main()
