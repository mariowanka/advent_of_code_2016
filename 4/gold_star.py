from silver_star import RoomDecrypter, INFILE

class GoldRoomDecrpter(RoomDecrypter):
    def __init__(self):
        super(GoldRoomDecrpter, self).__init__()
        self.alpha = "abcdefghijklmnopqrstuvwxyz"

    def decrypt_name(self, line):
        res = ""

        for c in " ".join(line["name"]):
            if c in self.alpha:
                res += self.alpha[(self.alpha.index(c) + line["id"]) % 26]
            else:
                res += c

        return res

if __name__ == "__main__":
    gdec = GoldRoomDecrpter()
    for line in gdec.read_input(INFILE):
        if gdec.is_real_room(line):
            name = gdec.decrypt_name(line)
            if "north" in name:
                print line["id"], name