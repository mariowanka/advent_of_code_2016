import sys
import string
import random
import md5

class PassCracker(object):
    def __init__(self):
        self.door = "ffykfhsq"
        self.passwd = [ None for x in xrange(8) ]

        self.rounds = 10000000000

    def _try_hash(self):
        for i in xrange(self.rounds):
            yield md5.new(self.door+str(i)).hexdigest()

    def _is_hash_valid(self, hash):
        return True if hash[:5] == "00000" else False

    def _print_cracker(self):
        for x in self.passwd:
            if x is None:
                print random.choice(string.ascii_letters),
            else:
                print x,
        print "\r"

        sys.stdout.flush()

    def crack(self):
        pos = 0
        for i, res in enumerate(self._try_hash()):
            if self._is_hash_valid(res):
                self.passwd[pos] = res[5]
                pos += 1
                if pos == 7:
                    self._print_cracker()
                    break

            if not i%100:
                self._print_cracker()


if __name__ == "__main__":
    cracker = PassCracker()
    cracker.crack()