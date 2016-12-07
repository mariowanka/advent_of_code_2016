from silver_star import Trianglonator, INFILE

class GoldTrianglonator(Trianglonator):
    def __init__(self):
        self.valid_count = 0

    def parse_block(self, block):
        for i in xrange(3):
            if self.is_valid(block[0][i], block[1][i], block[2][i]):
                self.valid_count += 1

    def parse_input_per_block(self):
        with open(INFILE) as file_in:
            block = []
            lines_in_block = 0
            for line in file_in.readlines():
                block.append(map(int, line.split()))
                lines_in_block +=1

                if lines_in_block == 3:
                    self.parse_block(block)
                    block = []
                    lines_in_block = 0

if __name__ == "__main__":
    gtgn = GoldTrianglonator()
    gtgn.parse_input_per_block()
    print gtgn.valid_count