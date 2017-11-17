INFILE = "in"

class Decompressor(object):
    def __init__(self):
        self.input = None
        self.input_len = None
        self.msg = ""

        self.read_input(INFILE)

    def read_input(self, in_file):
        with open(in_file) as file_in:
            self.input = file_in.readline()

        self.input_len = len(self.input)

    def decompress(self):
        i = 0
        while True:
            if self.input[i] != "(":
                self.msg += self.input[i]
                i+=1
            else:
                count, rep, i = self.parse_coding(i)
                app = self.input[i:i+count]
                self.msg += app*rep
                i += count

            if i >= self.input_len:
                break;

    # length of repetition, number od repetitions and "pointer" to first character after parenthesis
    def parse_coding(self, i):
        x = i

        # get end of parenthesis
        while self.input[x] != ")":
            x += 1

        vals = self.input[i+1:x].split("x")
        return int(vals[0]), int(vals[1]), x+1


if __name__ == "__main__":
    dec = Decompressor()
    dec.decompress()

    print len(dec.msg)
