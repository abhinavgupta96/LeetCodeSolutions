class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        # for i in range(len(nums)):
        #     totalSum = 0
        #     for j in range(i, len(nums)):
        #         totalSum += nums[j]
        #         if totalSum == k:
        #             result +=1
        # return result
        
        prefixSum = defaultdict(int)
        prefixSum[0] = 1

        currentSum = 0
        for num in nums:
            currentSum += num
            if (currentSum - k) in prefixSum:
                result += prefixSum[currentSum - k]
            prefixSum[currentSum]+=1
        return result
        