import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.vals = []
        self.locs = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.vals.append(val)
        self.locs[val].add(len(self.vals) - 1)
        return len(self.locs[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.locs[val]:
            return False

        loc = self.locs[val].pop()
        last = self.vals[-1]

        self.vals[loc] = last
        self.locs[last].add(loc)
        self.locs[last].discard(len(self.vals) - 1)
        self.vals.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)