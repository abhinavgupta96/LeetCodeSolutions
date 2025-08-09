class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        maxSeq = 0
        tempset = set()
        
        while r<len(s):
            if s[r] not in tempset:
                tempset.add(s[r])
                maxSeq = max(maxSeq, (r-l+1))
                r+=1
            else:
                tempset.remove(s[l])
                l+=1
        return maxSeq

