class RandomizedSet:

    def __init__(self):
        self.valueindex = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.valueindex:
            return False
        self.valueindex[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.valueindex:
            return False
        lastelement,removeidx = self.values[-1],self.valueindex[val]
        self.values[removeidx],self.valueindex[lastelement] = lastelement,removeidx
        del self.valueindex[val]
        self.values.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
