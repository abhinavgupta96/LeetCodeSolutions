class Solution:
    def longestPalindrome(self, s: str) -> str:
        resultString = ""
        resultLen = 0

        #for odd length palindromes
        for i in range(len(s)):
            l=r=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 > resultLen:
                    resultString = s[l:r+1]
                    resultLen = r-l+1
                l-=1
                r+=1
        
        #for even length palindromes
        for i in range(len(s)):
            l = i
            r = i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 > resultLen:
                    resultString = s[l:r+1]
                    resultLen = r-l+1
                l-=1
                r+=1
        return resultString