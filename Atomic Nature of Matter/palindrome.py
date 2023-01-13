import stdio
import sys


# Entry point [DO NOT EDIT].
def main():
    s = sys.argv[1]
    stdio.writeln(isPalindrome(s))


# Returns True if s is a palindrome, and False otherwise.
def isPalindrome(s):
    # Base case: if s is the empty string, return True.
    if s == '':
        return True

    # Recursive step: return True if the first and last characters of s are the same and
    # isPalindrome(characters between first and last in s) is True; and False otherwise.
    if s[0] == s[len(s) - 1] and isPalindrome(s[1:len(s) - 1]):
        return True
    return False


if __name__ == '__main__':
    main()
