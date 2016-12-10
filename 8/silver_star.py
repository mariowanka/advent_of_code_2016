INFILE = "in"

class DisplayExecuter(object):
    def __init__(self):
        self.display_width = 50
        self.display_hight = 6

        self.display = { (x, y): 0 for x in xrange(self.display_width) for y in xrange(self.display_hight) }
        self.instr = {
            "turn_on": self.turn_on,
            "rotate_col": self.rotate_col,
            "rotate_row": self.rotate_row
        }

    def parse_func(self, f):
        def parse_rect(line):
            params = map(int, line.split()[1].split("x"))
            return params[0], params[1]

        def parse_rotate(line):
            parts = line.split()
            a = int(parts[2].split("=")[1])
            b = int(parts[4])
            return a, b

        if "rect" in f:
            a, b = parse_rect(f)
            return "turn_on", a, b
        elif "column" in f:
            a, b = parse_rotate(f)
            return "rotate_col", a, b
        elif "row" in f:
            a, b = parse_rotate(f)
            return "rotate_row", a, b

    def turn_on(self, x, y):
        for a in xrange(x):
            for b in xrange(y):
                self.display[(a, b)] = 1

    def rotate_col(self, x, cnt):
        def rotate(x):
            carry = carry = self.display[x, self.display_hight-1]

            for i in xrange(self.display_hight-1, -1, -1):
                self.display[x, i] = self.display[x, i-1] if i != 0 else carry

        for i in xrange(cnt):
            rotate(x)

    def rotate_row(self, y, cnt):
        def rotate(y):
            carry = carry = self.display[self.display_width-1, y]

            for i in xrange(self.display_width-1, -1, -1):
                self.display[i, y] = self.display[i-1, y] if i != 0 else carry

        for i in xrange(cnt):
            rotate(y)

    def get_on_count(self):
        return sum(self.display.values())


if __name__ == "__main__":
    exc = DisplayExecuter()

    with open(INFILE) as file_in:
        for line in file_in.readlines():
            instr, a, b = exc.parse_func(line)
            exc.instr[instr](a, b)

    print exc.get_on_count()