INFILE = "in"

class BathCode(object):
    def __init__(self):
        self.inst = None
        self._read_input(INFILE)

        self.keypad = {
            (0, 0): 1,
            (1, 0): 2,
            (2, 0): 3,
            (0, 1): 4,
            (1, 1): 5,
            (2, 1): 6,
            (0, 2): 7,
            (1, 2): 8,
            (2, 2): 9
        }

        self.pos = [1, 1]

    def _read_input(self, in_file):
        res = []
        with open(in_file) as file_in:
            for line in file_in.readlines():
                data = [ inst for inst in line ]

                res.append(data)

        self.inst = res

    def move(self, inst):
        if inst == "U" and self.pos[1]>0:
            self.pos[1] -= 1
        elif inst == "D" and self.pos[1]<2:
            self.pos[1] += 1
        elif inst == "L" and self.pos[0]>0:
            self.pos[0] -= 1
        elif inst == "R" and self.pos[0]<2:
            self.pos[0] += 1

        return self.pos

    def get_code(self):
        res = []

        for line in self.inst:
            for inst in line:
                self.move(inst)

            res.append(self.keypad[tuple(self.pos)])

        return res


if __name__ == "__main__":
    decoder = BathCode()
    print decoder.get_code()
