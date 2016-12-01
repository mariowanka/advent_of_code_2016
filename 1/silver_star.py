INFILE = "in"

class Traveler(object):
    """
    Class implementing figure on map, that is able tu turn and go straight ahead.
    """
    def __init__(self, course, pos):
        self.course = course
        self.pos = pos

        self.left_turn = {
            "N": "W",
            "W": "S",
            "S": "E",
            "E": "N"
        }
        self.right_turn = {
            "N": "E",
            "E": "S",
            "S": "W",
            "W": "N"
        }

    def left(self):
        self.course = self.left_turn[self.course]

    def right(self):
        self.course = self.right_turn[self.course]

    def step(self, steps):
        if self.course == "N":
            self.pos[1] += steps
        elif self.course == "S":
            self.pos[1] -= steps
        elif self.course == "E":
            self.pos[0] += steps
        elif self.course == "W":
            self.pos[0] -= steps


class MapResolver(object):
    def __init__(self):
        self.inst = None
        self._read_input(INFILE)

        self.traveler = Traveler("N", [0, 0])

    def _read_input(self, in_file):
        """
        Read input text file and return list of tuples ofinstructions.
        """
        data = None
        with open(in_file) as file_in:
            data = file_in.read()

        self.inst = [ (inst[0], int(inst[1:])) for inst in data.split(", ") ]

    def move(self, turn, distance):
        if turn == 'R':
            self.traveler.right()
        elif turn == 'L':
            self.traveler.left()

        self.traveler.step(distance)

        return self.traveler.pos

    def get_hq_coords(self, ):
        for inst in self.inst:
            self.move(inst[0], inst[1])

        return self.traveler.pos

    def get_distance(self, fin, start=[0, 0]):
        return abs(fin[0]-start[0]) + abs(fin[1]-start[1])


if __name__ == "__main__":
    resolver = MapResolver()
    print resolver.get_distance(resolver.get_hq_coords())



('R', 4) # E [4, 0]
('R', 3) # S [4, -3]
('L', 3) # E [7, -3]
('L', 2) # N [7, -1]
('L', 1) # W [6, -1]
('R', 1) # N [6, 0]
('L', 1) # W [5, 0]
('R', 2) # N [5, 2]
('R', 3) # E [8, 2]
('L', 5) # N [8, 7]
('L', 5) # W [3, 7]