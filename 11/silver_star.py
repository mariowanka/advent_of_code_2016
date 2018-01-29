from copy import deepcopy

INFILE = "in"

# add-hoc dictionary for known parts
GENERATORS = {
    "thulium generator": "thg",
    "plutonium generator": "plg",
    "strontium generator": "stg",
    "promethium generator": "prg",
    "ruthenium generator": "rug",
}
CHIPS = {
    "thulium-compatible microchip": "thc",
    "plutonium-compatible microchip": "plc",
    "strontium-compatible microchip": "stc",
    "promethium-compatible microchip": "prc",
    "ruthenium-compatible microchip": "ruc"
}

# single state is defined as dict floor: set of parts
class Factory(object):
    def __init__(self):
        self.state = {} # actual state
        self.queue = [] # list of sattes to try
        self.visited = [] # list of states already tried
        self.step_map = {} # steps: [list of states]

        self._initialize()

    # read infile and generate initial state
    def _initialize(self):
        self.state["elev"] = 1 # position of elevator
        self.state[1] = {"gen": set([]), "chip": set([])}
        self.state[2] = {"gen": set([]), "chip": set([])}
        self.state[3] = {"gen": set([]), "chip": set([])}
        self.state[4] = {"gen": set([]), "chip": set([])}

        with open(INFILE) as file_in:
            for i, line in enumerate(file_in.readlines(), 1):
                for part in GENERATORS:
                    if part in line:
                        self.state[i]["gen"].add(GENERATORS[part])
                for part in CHIPS:
                    if part in line:
                        self.state[i]["chip"].add(CHIPS[part])

    # generate all neighbour states of actual one
    # yield one at time
    def expand(self):
        level = self.state["elev"]
        floor = self.state[level]

        # try move all present chips
        for chip in floor["chip"]:
            # chip alone
            if level != 1:
                new_state = deepcopy(self.state)
                new_state[level][chip].remove(chip)
                new_state[level-1][chip].add(chip)


        #try nove all present generators
        for gen in floor["gen"]

    # all parts are in fourth floor
    def finished(self):
        # all parts in assembler
        if self.state["elev"] == 4 and self.state[4] and not self.state[1] and not self.state[2] and not self.state[3]:
            return True
        else:
            return False

    # no part will be fried in such state
    def is_valid(self, state):
        for floor in self.state.values():
            # when generator present all chips have generators
            if floor["gen"]:
                for chip in floor["chip"]:
                    if not chip in floor["gen"]:
                        return False

        return True

    # search in state map for given state
    def get_steps(self, state):
        for steps in self.step_map:
            if state in self.step_map[steps]:
                return steps

        return None

    # run the assembly process - expand the states in breadth-first-search
    def assemble(self):
        while True:
            steps = get_steps(self.state)

            if self.finished():
                return steps
            else:
                self.visited.append(self.state)
                steps += 1

            # generate new states
            for layout in self.expand():
                # new state
                if self.state not in self.visited or self.state not in self.queue:
                    self.queue.insert(0, self.state)
                    self.step_map[steps] = state

            # get next state
            self.state = self.queue.pop()


if __name__ == "__main__":
    factory = Factory()
    print factory.assemble()