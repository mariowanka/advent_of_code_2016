from silver_star import INFILE
from silver_star import BroadcastFixer

class GoldBroadcastFixer(BroadcastFixer):
    def get_least_common(self, char_dict):
        res = None
        res_count = None

        for c in char_dict:
            if res_count is None:
                res = c
                res_count = char_dict[c]
            elif char_dict[c] < res_count:
                    res = c
                    res_count = char_dict[c]

        return res


if __name__ == "__main__":
    fixer = GoldBroadcastFixer()

    with open(INFILE) as file_in:
        for line in file_in.readlines():
            fixer.load_line(line)

    print fixer.get_msg(fixer.get_least_common)

