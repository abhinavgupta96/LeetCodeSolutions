class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l =0
        r = 0
        maxLen = 0
        tempset = set()
        while r<len(s):
            if s[r] not in tempset:
                tempset.add(s[r])
                strLen = r-l+1
                maxLen = max(maxLen, strLen)
                r+=1
            else:
                tempset.remove(s[l])
                l+=1
        return maxLen
