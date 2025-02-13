class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        output = []
        minLen = min(n,m)
        for i in range(minLen):
            output.append(word1[i])
            output.append(word2[i])
        
        if n > m:
            output.append(word1[minLen:])
        else:
            output.append(word2[minLen:])
        return "".join(output)