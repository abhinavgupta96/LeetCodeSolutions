class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, result = set(), set()
        for i in range(len(s)-9):
            curr = s[i:i+10]
            if curr in seen:
                result.add(curr)
            seen.add(curr)
        return list(result)