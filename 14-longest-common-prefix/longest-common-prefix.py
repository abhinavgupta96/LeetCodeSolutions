class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # Remove the last character
                if not prefix:
                    return ""  # No common prefix
        
        return prefix