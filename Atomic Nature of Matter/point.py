import stdio
import sys


# A data type to represent a point in 2D space.
class Point:

    # Constructs a new point given its x and y coordinates.
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Returns the Euclidean distance between this point and other.
    def distanceTo(self, other):
        c1 = (other.x - self.x) ** 2
        c2 = (other.y - self.y) ** 2
        return (c1 + c2) ** 0.5

    # Return a string representation of this point.
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


# Test client [DO NOT EDIT].
def _main():
    x1, y1, x2, y2 = map(float, sys.argv[1:])
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    stdio.writeln('p1        = ' + str(p1))
    stdio.writeln('p2        = ' + str(p2))
    stdio.writeln('d(p1, p2) = ' + str(p1.distanceTo(p2)))


if __name__ == '__main__':
    _main()
