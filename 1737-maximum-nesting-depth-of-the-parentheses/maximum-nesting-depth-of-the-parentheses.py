class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        curr = 0

        for c in s:
            if c=="(":
                curr +=1
            elif c==")": 
                curr-=1
            res = max(curr, res)
        return res
        