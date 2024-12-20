class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def dfs(s,k):
            freq_count = collections.Counter(s)
            for i, c in enumerate(s) :
                  if freq_count[c] < k:
                    left = dfs(s[:i],k)
                    right = dfs(s[i+1:],k)
                    return max(left, right)
            return len(s)
        return dfs(s,k)
        