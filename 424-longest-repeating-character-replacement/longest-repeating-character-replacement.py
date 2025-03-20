class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        counter = {}
        result = 0
        maxf = 0
        for r in range(len(s)):
            counter[s[r]] = 1 + counter.get(s[r], 0)
            maxf = max(maxf, counter[s[r]])

            while (r-l+1) - maxf > k:
                counter[s[l]]-=1
                l+=1
    
            result = max(result, r-l+1)
        return result