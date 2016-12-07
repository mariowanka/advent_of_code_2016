INFILE = "in"
LINELENGTH = 8

class BroadcastFixer(object):
    def __init__(self):
        self.msg = [ {} for x in xrange(LINELENGTH) ]

    def load_line(self, line):
        for i in xrange(LINELENGTH):
            c = line[i]
            if c in self.msg[i]:
                self.msg[i][c] += 1
            else:
                self.msg[i][c] = 1

    def get_most_common(self, char_dict):
        res = None
        res_count = 0

        for c in char_dict:
            if char_dict[c] > res_count:
                res = c
                res_count = char_dict[c]

        return res

    def get_msg(self, decoder):
        res = ""
        for i in xrange(LINELENGTH):
            res += decoder(self.msg[i])
        return res


if __name__ == "__main__":
    fixer = BroadcastFixer()

    with open(INFILE) as file_in:
        for line in file_in.readlines():
            fixer.load_line(line)

    print fixer.get_msg(fixer.get_most_common)
