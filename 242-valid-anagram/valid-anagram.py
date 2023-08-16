class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t) : 
            hashS = {}
            hashT = {}
            return sorted(s)==sorted(t)
        else:
            return False
        