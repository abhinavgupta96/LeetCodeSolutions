class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        partList = p.split("*")
        i = 0
        for part in partList:
            j = s.find(part, i)
            if j == -1:
                return False
            i = j+len(part)
        return True
