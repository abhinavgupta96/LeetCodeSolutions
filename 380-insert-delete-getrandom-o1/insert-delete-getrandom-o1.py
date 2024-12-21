
class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.map = {}
        # map stores value to index

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val]=len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        idx = self.map[val]
        last_element = self.arr[-1]
        self.arr[idx] = last_element
        self.map[last_element]=idx
        del self.map[val]
        self.arr.pop()
        return True
        

    def getRandom(self) -> int:
        return self.arr[randint(0, len(self.arr)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()