INFILE = "in"

class Trianglonator(object):
    def __init__(self):
        pass

    def is_valid(self, a, b, c):
        return True if a+b>c and a+c>b and b+c>a else False


if __name__ == "__main__":
    tgn = Trianglonator()
    res = 0

    with open(INFILE) as file_in:
        for line in file_in.readlines():
            if tgn.is_valid(*map(int, line.split())):
                res += 1

    print res