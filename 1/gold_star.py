INFILE = "in"

from silver_star import MapResolver

class GoldenResolver(MapResolver):
    def __init__(self):
        super(GoldenResolver, self).__init__()
        self.visited = [[0, 0]]

    def get_first_cross(self):
        """
        Move through map until you hit position once visited.
        """
        for inst in self.inst:
            self.move(inst[0], 0) # just a turn

            for step in xrange(inst[1]):
                # and the move
                pos = self.move(None, 1)

                if pos in self.visited:
                    return pos
                else:
                    self.visited.append(list(pos))

if __name__ == "__main__":
    resolver = GoldenResolver()
    print resolver.get_distance(resolver.get_first_cross())
