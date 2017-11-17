INFILE = "in"

class Decompressor(object):
    def __init__(self):
        self.input = None

        self.read_input(INFILE)

    def read_input(self, in_file):
        with open(in_file) as file_in:
            self.input = file_in.readline()

        self.input_len = len(self.input)

    # parse single message
    def decompress(self, msg):
        i = 0
        length = 0
        input_len = len(msg)

        while True:
            if msg[i] != "(":
                length += 1
                i += 1
            else:
                i, msg_len = self.parse_data(i, msg)
                length += msg_len

            if i >= input_len:
                return length

    # count length of nested message
    # i - pointer to opening parenthesis
    # return pointer to first character after message and it's encoded length
    def parse_data(self, i, msg):
        rep, start, end = self.get_coding(i, msg)
        return end, len(msg[start:end]*rep)

    # number od repetitions, "pointer" to first and last character after parenthesis
    def get_coding(self, i, msg):
        x = i

        # get end of parenthesis
        while msg[x] != ")":
            x += 1

        vals = msg[i+1:x].split("x")
        count = int(vals[0])
        rep = int(vals[1])
        start = x+1
        end = start+count

        return rep, start, end

if __name__ == "__main__":
    dec = Decompressor()
    print dec.decompress(dec.input)
