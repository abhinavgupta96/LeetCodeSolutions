class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        result = 0
        currMax = values[0]-1

        for i in range(1, len(values)):
            result = max(result, currMax + values[i])
            currMax = max(currMax-1, values[i]-1)
        return result