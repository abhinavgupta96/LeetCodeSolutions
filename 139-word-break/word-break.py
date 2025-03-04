class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        q = deque([0])
        seen = set()
        wordDict = set(wordDict)

        while q:
            start = q.popleft()
            if start in seen:
                continue
            seen.add(start)
            for end in range(start+1, len(s)+1):
                if s[start:end] in wordDict:
                    if end == len(s):
                        return True
                    q.append(end)
        return False

                    