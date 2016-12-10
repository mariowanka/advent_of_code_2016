from functools import partial
from silver_star import INFILE, TlsDetector

class GoldTlsDetector(TlsDetector):
    def get_ssl_tokens(self, s):
        for i in xrange(len(s)-2):
            if s[i]==s[i+2] and s[i]!=s[i+1]:
                yield s[i:i+3]

    def has_reversed_ssl(self, token, s):
        rev = token[1]+token[0]+token[1]
        return True if rev in s else False

    def supports_ssl(self, addr):
        supernet, hypernet = self.split_addr(addr)
        for part in supernet:
            for token in self.get_ssl_tokens(part):
                func = partial(self.has_reversed_ssl, token)
                if any(map(func, hypernet)):
                    return True
        return False


if __name__ == "__main__":
    gtd = GoldTlsDetector()
    with open(INFILE) as file_in:
        for line in file_in.readlines():
            if gtd.supports_ssl(line):
                gtd.supported += 1

    print gtd.supported