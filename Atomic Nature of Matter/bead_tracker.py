import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture


# Entry point
def main():
    # Get an integer, pixels, and two floats, tau and delta, from command line.
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])

    # Create a BlobFinder object for the frame (Picture object) from command line.
    pic = Picture(sys.argv[4])
    bf = BlobFinder(pic, tau)

    # Get a list of beads from bf.
    prevBeads = bf.getBeads(pixels)

    for f in sys.argv[5:]:
        # For each frame starting at sys.argv[5]...

        # ...create a BlobFinder object and get a list of beads, currBeads,
        # that have at least pixels pixels.
        nbf = BlobFinder(Picture(f), tau)
        currBeads = nbf.getBeads(pixels)

        for currBead in currBeads:
            # ...For each currBead in currBeads...

            # ...create an empty list that stores beads that are no farther than
            # delta.
            close_d = []

            # ...for each prevBead in prevBeads...
            for prevBead in prevBeads:
                # ...find a d(distance between currBead and prevBead)
                d = currBead.distanceTo(prevBead)

                # ...if d is less than delta...
                if d < delta:
                    # ...add that d to the close_d list.
                    close_d.append(d)
            # ...After getting all the beads that are no farther than delta...

            # ...if len(close_d) is greater than 0...
            if len(close_d) > 0:
                # ...Get the minimum value of close_d which is the closest to currBead.
                d = min(close_d)
                # ...write that value of d.
                stdio.writef('%.4f\n', d)
        # ...Write a newline character.
        stdio.writeln()
        # ...Set prevBeads to currBeads
        prevBeads = currBeads


if __name__ == '__main__':
    main()
