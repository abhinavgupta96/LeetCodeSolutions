class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        res = 0
        curr = 0

        for c in s:
            if c=="(":
                curr+=1
                res = max(curr, res)
            elif c == ")":
                curr-=1
            
        return res