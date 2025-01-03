class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # wordSet = set(wordDict)
        # q = deque([0])
        # visit = set()

        # while q:
        #     start = q.popleft()
        #     if start == len(s):
        #         return True
        #     visit.add(start)
        #     for end in range(start+1, len(s)+1):
        #         if s[start:end] in wordSet:
        #             if end==len(s):
        #                 return True
        #             q.append(end)
        # return False
        # def dfs(i):
        #     if i == len(s):
        #         return True
            
        #     for w in wordDict:
        #         if ((i + len(w)) <= len(s) and 
        #              s[i : i + len(w)] == w
        #         ):
        #             if dfs(i + len(w)):
        #                 return True
        #     return False
        
        # return dfs(0)
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]

