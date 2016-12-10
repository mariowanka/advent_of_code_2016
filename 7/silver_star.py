INFILE = "in"

class TlsDetector(object):
    def __init__(self):
        self.supported = 0

    def is_abba(self, s):
        for i in xrange(len(s)-3):
            if s[i]==s[i+3] and s[i+1]==s[i+2] and s[i]!=s[i+1]:
                return True
        return False

    def is_not_abba(self, s):
        return not self.is_abba(s)

    def split_addr(self, addr):
        """
        split address into two lists - hypernet (in brackets), supernet (out of brackets)
        """
        hypernet = []
        supernet = []

        addr = addr.split("[")
        for part in addr:
            if "]" in part:
                hypernet.append(part.split("]")[0])
                supernet.append(part.split("]")[1])
            else:
                supernet.append(part)

        return supernet, hypernet

    def supports_tls(self, addr):
        supernet, hypernet = self.split_addr(addr)
        return any(map(self.is_abba, supernet)) and all(map(self.is_not_abba, hypernet))


if __name__ == "__main__":
    td = TlsDetector()
    with open(INFILE) as file_in:
        for line in file_in.readlines():
            if td.supports_tls(line):
                td.supported +=1

    print td.supported