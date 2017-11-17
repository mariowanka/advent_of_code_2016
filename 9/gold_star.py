from silver_star import INFILE, Decompressor

class GoldDecompressor(Decompressor):
    # add recursive decoding to nestet messages
    def parse_data(self, i, msg):
        rep, start, end = self.get_coding(i, msg)

        # bottom of recursion
        if "(" not in msg[start:end]:
            return end, len(msg[start:end]*rep)

        # dig deeper
        else:
            return end, self.decompress(msg[start:end])*rep

if __name__ == "__main__":
    gdec = GoldDecompressor()
    print gdec.decompress(gdec.input)
