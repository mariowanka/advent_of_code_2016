INFILE = "in"

from silver_star import BathCode

class GoldBath(BathCode):
    def __init__(self):
        super(GoldBath, self).__init__()

        self.pos = [1, 3]

        self.keypad = {
            (x, y): None for x in xrange(7) for y in xrange(7)
        }

        self.keypad[(3, 1)] = "1"
        self.keypad[(2, 2)] = "2"
        self.keypad[(3, 2)] = "3"
        self.keypad[(4, 2)] = "4"
        self.keypad[(1, 3)] = "5"
        self.keypad[(2, 3)] = "6"
        self.keypad[(3, 3)] = "7"
        self.keypad[(4, 3)] = "8"
        self.keypad[(5, 3)] = "9"
        self.keypad[(2, 4)] = "A"
        self.keypad[(3, 4)] = "B"
        self.keypad[(4, 4)] = "C"
        self.keypad[(3, 5)] = "D"

    def move(self, inst):
        if inst == "U" and self.keypad[tuple([self.pos[0], self.pos[1]-1])] is not None:
            self.pos[1] -= 1
        elif inst == "D" and self.keypad[tuple([self.pos[0], self.pos[1]+1])] is not None:
            self.pos[1] += 1
        elif inst == "L" and self.keypad[tuple([self.pos[0]-1, self.pos[1]])] is not None:
            self.pos[0] -= 1
        elif inst == "R" and self.keypad[tuple([self.pos[0]+1, self.pos[1]])] is not None:
            self.pos[0] += 1


if __name__ == "__main__":
    decoder = GoldBath()
    print decoder.get_code()
