from silver_star import INFILE, DisplayExecuter

class GoldDisplayExecuter(DisplayExecuter):
    def __init__(self):
        super(GoldDisplayExecuter, self).__init__()
        self.letter = 5

    def show(self):
        for i in xrange(0, self.display_width, 5):
            self.show_letter(i)

    def show_letter(self, i):
        for y in xrange(0, self.display_hight):
            for x in xrange(i, i+5):
                print "#" if self.display[(x, y)] else "-",
            print ""
        print "\n\n"


if __name__ == "__main__":
    exc = GoldDisplayExecuter()

    with open(INFILE) as file_in:
        for line in file_in.readlines():
            instr, a, b = exc.parse_func(line)
            exc.instr[instr](a, b)

    exc.show()
