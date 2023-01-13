import stdio
import sys


# Entry point [DO NOT EDIT].
def main():
    s = sys.argv[1]
    stdio.writeln(reverse(s))


# Returns the reverse of the string s.
def reverse(s):
    # Base case: if s is the empty string, return an empty string.
    if s == '':
        return ''

    # Recursive step: return last character in s + reverse(s excluding last character).
    return s[len(s) - 1] + reverse(s[:len(s) - 1])


if __name__ == '__main__':
    main()
