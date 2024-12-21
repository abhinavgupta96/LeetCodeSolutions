
class RandomizedSet:

    def __init__(self):
        self.size=0
        self.map = {}
        

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val]=1
        self.size+=1
        return True

    def remove(self, val: int) -> bool:
        if val in self.map:
            del self.map[val]
            self.size-=1
            return True
        return False
        

    def getRandom(self) -> int:
        idx = random.randint(0, self.size-1)
        return list(self.map.keys())[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()