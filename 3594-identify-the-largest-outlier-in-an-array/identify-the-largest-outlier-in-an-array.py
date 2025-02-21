class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        freqMap = Counter(nums)
        totalSum = sum(nums)
        largestOutlier = -inf

        for num, freq in freqMap.items():
            tentativeSum = totalSum - num
            if tentativeSum %2 or freqMap[tentativeSum//2] == 0:
                continue
            
            if num!=tentativeSum//2 or freq>1:
                largestOutlier = max(largestOutlier, num)
            
        return largestOutlier