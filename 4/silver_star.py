INFILE = "in"

class RoomDecrypter(object):
    def __init__(self):
        self.id_sum = 0

    def read_input(self, in_file):
        with open(in_file) as file_in:
            for line in file_in.readlines():
                yield self._parse_line(line)

    def _parse_line(self, line):
        return {
            "name": line.split("-")[:-1],
            "id": int(line.split("-")[-1:][0].split("[")[0]),
            "checksum" : line[-7:-2]
        }

    def is_real_room(self, line):
        name = "".join(line["name"])
        char_counts = {}
        res = ""

        for c in name:
            if c in char_counts:
                char_counts[c] += 1
            else:
                char_counts[c] = 1

        for x in xrange(5):
            c_of_check = self._get_most_common(char_counts)
            char_counts.pop(c_of_check)
            res += c_of_check

        return True if res == line["checksum"] else False

    def _get_most_common(self, chars):
        res = {"char": None, "vol": 0}

        for c in chars:
            if chars[c] > res["vol"] or (chars[c] == res["vol"] and c < res["char"]):
                res["char"] = c
                res["vol"] = chars[c]

        return res["char"]



if __name__ == "__main__":
    dec = RoomDecrypter()
    for line in dec.read_input(INFILE):
        if dec.is_real_room(line):
            dec.id_sum += line["id"]

    print dec.id_sum