import stdio
import stdrandom
import sys


# Generates and returns the public/private keys as a tuple (n, e, d). Prime numbers p and q
# needed to generate the keys are picked from the interval [lo, hi).
def keygen(lo, hi):
    # Get a list of primes from the interval [lo,hi) by calling the function _primes()
    primes = _primes(lo, hi)

    # Call the function _sample() applying to the list of primes with k = 2,
    # therefore, assign the two random primes of the list to variables p and q
    sample = _sample(primes, 2)
    p, q = sample[0], sample[1]

    # Set n to pq.
    n = p * q
    # Set m to (p-1)(q-1)
    m = (p - 1) * (q - 1)

    # Call the function _choice() and get a random
    # value of the list of primes from the interval [2,m).
    e = _choice(_primes(2, m))
    if m % e != 0:
        # if m mod e is not 0, that is the value of e...
        pass
    else:
        # ...otherwise, as long as m mod e is equal 0, keep searching
        # the value of e that satisfy the condition.
        while m % e == 0:
            e = _choice(_primes(2, m))

    # Get a random value of d from interval [1,m).
    d = stdrandom.uniformInt(1, m)

    # if ed mod m is equal 1, that is the value of d...
    if (e * d) % m == 1:
        pass

    # ...otherwise, as long as ed mod m is not equal to 1, keep searching
    # the value of d that satisfy the condition.
    else:
        while (e * d) % m != 1:
            d = stdrandom.uniformInt(1, m)

    # Create a tuple (n, e, d) and return it.
    keys = (n, e, d)
    return keys


# Encrypts x (int) using the public key (n, e) and returns the encrypted value.
def encrypt(x, n, e):
    # The formula used to encrypt x.
    encrypts = (x ** e) % n
    return encrypts


# Decrypts y (int) using the private key (n, d) and returns the decrypted value.
def decrypt(y, n, d):
    # The formula used to decrypt y.
    decrypts = (y ** d) % n
    return decrypts


# Returns the least number of bits needed to represent n.
def bitLength(n):
    return len(bin(n)) - 2


# Returns the binary representation of n expressed in decimal, having the given width, and padded
# with leading zeros.
def dec2bin(n, width):
    return format(n, '0%db' % (width))


# Returns the decimal representation of n expressed in binary.
def bin2dec(n):
    return int(n, 2)


# Returns a list of primes from the interval [lo, hi).
def _primes(lo, hi):
    # create an empty list.
    primes_list = []
    for p in range(lo + 2, hi):
        # for each p from [lo + 2, hi]...

        # Set j (potential divisor of i) to 2.
        j = 2
        while j <= p / j:
            # As long as j is less than or equal to p / j...

            if p % j == 0:
                # If j divides p, break (i is not a prime).
                break

            # Increment j by 1.
            j += 1

        # If you got here by exhausting the while loop, i is a prime...
        if j > p / j:
            # ...so add p to the list.
            primes_list += [p]

    # Return the list.
    return primes_list


# Returns a list containing a random sample (without replacement) of k items from the list a.
def _sample(a, k):

    # Create a copy of the list a.
    b = []
    for v in a:
        b += [v]
    # Shuffle the list.
    stdrandom.shuffle(b)
    # Return a list containing the first k elements of b
    return b[:k]


# Returns a random item from the list a.
def _choice(a):
    # Set r to be a random number in the interval [0,len(a)](a is the given list)...
    r = stdrandom.uniformInt(0, len(a))
    # ...return an element of list a which its index is r.
    return a[r]


# Unit tests the library.
def _main():
    x = ord(sys.argv[1])
    n, e, d = keygen(25, 100)
    encrypted = encrypt(x, n, e)
    stdio.writef('encrypt(%c) = %d\n', x, encrypted)
    decrypted = decrypt(encrypted, n, d)
    stdio.writef('decrypt(%d) = %c\n', encrypted, decrypted)
    width = bitLength(x)
    stdio.writef('bitLength(%d) = %d\n', x, width)
    xBinary = dec2bin(x, width)
    stdio.writef('dec2bin(%d) = %s\n', x, xBinary)
    stdio.writef('bin2dec(%s) = %d\n', xBinary, bin2dec(xBinary))


if __name__ == '__main__':
    _main()
