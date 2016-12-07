from silver_star import PassCracker

class GoldPassCracker(PassCracker):
    def crack(self):
        for i, res in enumerate(self._try_hash()):
            if self._is_hash_valid(res) and res[5].isdigit() and int(res[5])<8 and self.passwd[int(res[5])] is None:
                self.passwd[int(res[5])] = res[6]

            if not i%100:
                self._print_cracker()

            if None not in self.passwd:
                self._print_cracker()
                break


if __name__ == "__main__":
    cracker = GoldPassCracker()
    cracker.crack()