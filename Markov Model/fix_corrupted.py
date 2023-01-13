from markov_model import MarkovModel
import stdio
import sys


# Entry point.
def main():
    # Get k(int) from command line
    k = int(sys.argv[1])

    # Get corrupted message (str) from command line
    corrupted = str(sys.argv[2])

    # Read text from standard input
    text = sys.stdin.read()

    # create a Markov model using text and k.
    model = MarkovModel(text, k)

    # Use the model to decode corrupted and write
    # the decoded message to standard output.
    stdio.writeln(model.replace_unknown(corrupted))


if __name__ == '__main__':
    main()
