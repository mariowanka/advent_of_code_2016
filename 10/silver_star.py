INFILE = "in"
FINAL_LOW = "17"
FINAL_HIGH = "61"

class Bot(object):
    def __init__(self, definition):
        self.number = None
        self.low_end = None # who gets lower value ("bot"/"output", number)
        self.high_end = None # who gets higher value ("bot"/"output", number)
        self.low = None # chip with lower value
        self.high = None # chip with higher value

        self._define(definition)


    # parse bot's definition
    def _define(self, definition):
        d = definition.split()

        self.number = d[1]
        self.low_end = tuple([d[5], d[6]])
        self.high_end = tuple([d[10], d[11]])

    # bot must decide which value is higher and keep that in mind
    def set_value(self, value, initialization=False):
        if value == self.low or value == self.high:
            return

        if self.low is None:
            self.low = value
        elif self.high is None:
            if self.low < value:
                self.high = value
            else:
                self.high = self.low
                self.low = value
        else:
            raise Exception("Bot "+str(self.number)+" cannot take anymore!")

        if not initialization:
            print "bot ", self.number, " has chips: ", self.low, " and ", self.high

    # with two chips bot can operate
    def has_both_chips(self):
        return True if (self.low is not None and self.high is not None) else False


class Factory(object):
    def __init__(self):
        self.instructions = []
        self.bots = {}
        self._create_bots()

    def _create_bots(self):
        # create bots
        with open(INFILE) as file_in:
            for line in file_in.readlines():
                # create bot
                if line.startswith("bot"):
                    bot = Bot(line)
                    self.bots[bot.number] = bot

                # add instruction on list
                line = line.split()
                self.instructions.append(tuple([line[0], line[1], line[5]])) # bot/value, id, bot's id for value

    # return number of bot which operated chips with values from instructions
    def work(self):
        print "Start work"
        while True: # run factory until some bot gets desired combination
            something_happend = False

            for inst in self.instructions:
                if inst[0] == "bot":
                    bot = self.bots[inst[1]]

                    if bot.has_both_chips():
                        # test ending condition
                        if bot.low == FINAL_LOW and bot.high == FINAL_HIGH:
                            return bot.number

                        # let bot do his job
                        self._transfer(bot)
                        something_happend = True

                    else:
                        print "bot ", bot.number, "has nothing to do"

                else: # value
                    bot = self.bots[inst[2]]
                    if not bot.has_both_chips():
                        bot.set_value(inst[1])
                        something_happend = True

            if not something_happend:
                print "!!! Factory deadlocked !!!"
                break

    # do whatever bot is supposed to do in his miserable existence
    def _transfer(self, bot):
        if bot.low_end[0] == "bot": # else let it disappear in output bin
            print "bot ", bot.number, " transfers chip ", bot.low, " to ", bot.low_end[0], " ", bot.low_end[1]
            self.bots[bot.low_end[1]].set_value(bot.low)
            bot.low = None
        else:
            print "bot ", bot.number, " gives chip ", bot.low, " to output"

        if bot.high_end[0] == "bot": # else let it disappear in output bin
            print "bot ", bot.number, " transfers chip ", bot.high, " to ", bot.high_end[0], " ", bot.high_end[1]
            self.bots[bot.high_end[1]].set_value(bot.high)
            bot.high = None
        else:
            print "bot ", bot.number, " gives chip ", bot.high, " to output"


if __name__ == "__main__":
    factory = Factory()
    print factory.work()
