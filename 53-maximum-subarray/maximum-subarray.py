class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        curr_sum = 0

        for n in nums:
            curr_sum =max(n, curr_sum+n)
            max_sum = max(max_sum, curr_sum)
        return max_sum