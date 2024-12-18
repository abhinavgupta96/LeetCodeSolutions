class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def dfs(s, k) : 
            if len(s)==0 :
                return 0

            freq = {}
            for char in s:
                if char in freq:
                    freq[char]+=1
                else:
                    freq[char]=1
            
            for i ,char in enumerate(s):
                if freq[char] < k:
                    left = dfs(s[:i], k)
                    right = dfs(s[i+1:], k)
                    return max(left, right)
            return (len(s))
        maxLen = dfs(s, k)
        return maxLen