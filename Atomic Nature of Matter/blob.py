import stdio


# A data type to represent a blob.
class Blob:
    # Constructs an empty blob.
    def __init__(self):
        # Initialize the instance variables, pixels to 0, x and y to 0.0
        self.pixels = 0
        self.x = 0.0
        self.y = 0.0

    # Adds pixel (x, y) to this blob.
    def add(self, x, y):
        # apply the running average formula to add a pixel to this blob.
        cx = self.x * self.pixels + x
        self.x = cx / (self.pixels + 1)
        cy = self.y * self.pixels + y
        self.y = cy / (self.pixels + 1)

        # Increment pixels by 1.
        self.pixels += 1

    # Returns the mass of this blob, ie, the number of pixels in it.
    def mass(self):
        # return pixels.
        return self.pixels

    # Returns the Euclidean distance between the center of mass of this blob and the center of
    # mass of the other blob.
    def distanceTo(self, other):
        # Apply the Euclidean distance formula.
        c1 = (other.x - self.x) ** 2
        c2 = (other.y - self.y) ** 2
        return (c1 + c2) ** 0.5

    # Returns a string representation of this blob.
    def __str__(self):
        return '%d (%.4f, %.4f)' % (self.pixels, self.x, self.y)


# Test client (DO NOT EDIT).
def _main():
    a = Blob()
    a.add(0, 0)
    b = Blob()
    while not stdio.isEmpty():
        x = stdio.readFloat()
        y = stdio.readFloat()
        b.add(x, y)
    stdio.writeln('a          = ' + str(a))
    stdio.writeln('b          = ' + str(b))
    stdio.writeln('dist(a, b) = ' + str(a.distanceTo(b)))


if __name__ == '__main__':
    _main()
