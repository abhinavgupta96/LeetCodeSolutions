class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 0
        self.data = [None]*n
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.data[idKey - 1] = value
        chunk = []

        while self.ptr<len(self.data) and self.data[self.ptr] is not None:
            chunk.append(self.data[self.ptr])
            self.ptr+=1
        return chunk
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)