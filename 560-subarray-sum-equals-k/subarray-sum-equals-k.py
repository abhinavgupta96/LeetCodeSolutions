class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        currSum = 0
        result = 0
        for i in nums:
            currSum +=i
            if currSum-k in prefixSum:
                result +=prefixSum[currSum - k]
            prefixSum[currSum]+=1
        
        return result