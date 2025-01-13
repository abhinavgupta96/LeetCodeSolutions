class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needleLen = len(needle)
        haystackLen = len(haystack)

        if needleLen > haystackLen:
            return -1
        
        for i in range(haystackLen - needleLen+1):
            j = 0
            while j < needleLen:
                if haystack[i+j] != needle[j]:
                    break
                j+=1
            if j == needleLen:
                return i
        return -1