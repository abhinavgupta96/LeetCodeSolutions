import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Initialize the answer array
        answer = [1] * n
        
        # Calculate the products of all elements to the left of each index
        left_product = 1
        for i in range(n):
            answer[i] *= left_product
            left_product *= nums[i]
        
        # Calculate the products of all elements to the right of each index
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        
        return answer

