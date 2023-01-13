from markov_model import MarkovModel
import stdio
import sys


# Entry point.
def main():
    # Get two integers, k and n, from command line.
    k = int(sys.argv[1])
    n = int(sys.argv[2])

    # read text from standard input.
    text = sys.stdin.read()

    # Create a Markov model using text and k.
    model = MarkovModel(text, k)

    # Write the random text to standard output by using self.gen() method.
    stdio.writeln(model.gen(text[:k], n))


if __name__ == '__main__':
    main()
