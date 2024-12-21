class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashDict = defaultdict(int)
        for c in s:
            hashDict[c]+=1
        for i,c in enumerate(s):
            if hashDict[c]==1:
                return i
        return -1
        