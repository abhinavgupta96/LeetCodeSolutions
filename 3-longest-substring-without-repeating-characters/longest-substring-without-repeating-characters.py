class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        set_str = set()
        res = 0
        for r in range(len(s)):
            while s[r] in set_str:
                set_str.remove(s[l])
                l+=1
            set_str.add(s[r])
            res = max(res, r-l+1)
        return res
        