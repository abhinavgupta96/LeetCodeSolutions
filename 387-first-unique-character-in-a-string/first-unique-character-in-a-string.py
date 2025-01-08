class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq_count = Counter(s)

        for i in range(len(s)):
            if freq_count[s[i]]==1:
                return i
        return -1