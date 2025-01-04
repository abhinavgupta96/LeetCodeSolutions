class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        q = deque([0])
        visit = set()

        while q : 
            start = q.popleft()
            if start in visit:
                continue
            visit.add(start)
            for end in range(start+1, len(s)+1):
                if s[start:end] in wordSet : 
                    if end==len(s):
                        return True
                    q.append(end)
        return False