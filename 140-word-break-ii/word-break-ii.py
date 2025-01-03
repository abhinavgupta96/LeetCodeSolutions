class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        
        def backtrack(i):
            if i==len(s):
                result.append(" ".join(curr))
                return
            
            for j in range(i, len(s)):
                w = s[i:j+1]
                if w in wordDict:
                    curr.append(w)
                    backtrack(j+1)
                    curr.pop()

        curr = []
        result = []
        backtrack(0)
        return result