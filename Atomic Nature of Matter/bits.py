import stdio
import sys


# Entry point. [DO NOT EDIT].
def main():
    s = sys.argv[1]
    stdio.writef('zeros = %d, ones = %d, total = %d\n', zeros(s), ones(s), len(s))


# Return the number of zeros in s.
def zeros(s):
    # Base case: if s is the empty string, return 0.
    if s == '':
        return 0

    # Recursive step: if the first character in s is 0, return 1 + zeros(rest of s). Otherwise,
    # return zeros(rest of s).
    if s[0] == '0':
        return 1 + zeros(s[1:])

    return zeros(s[1:])


# Return the number of ones in s.
def ones(s):
    # Base case: if s is the empty string, return 0.
    if s == '':
        return 0

    # Recursive step: if the first character in s is 1, return 1 + ones(rest of s). Otherwise,
    # return ones(rest of s).
    if s[0] == '1':
        return 1 + ones(s[1:])

    return ones(s[1:])


if __name__ == '__main__':
    main()
