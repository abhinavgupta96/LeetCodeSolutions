import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Initialize the answer array
        answer = [1] * n
        
        # Calculate the products of all elements to the left of each index
        # Since our final answer will be the result of prefix * postfix
        # In the first pass we calculate the prefix value for each element in the input
        # We also iteratively update the left product value after each calculation
        left_product = 1
        for i in range(n):
            answer[i] *= left_product
            left_product *= nums[i]
        
        # Calculate the products of all elements to the right of each index
        # The first pass will give us a the answer array with the prefix value for each of the element in the input array.
        # In this pass we calculate the postfix values for them, iteratively updating the right product values as well.
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        
        return answer
        #my approach - gives memory exceed error
        # prefix = [0 for i in range(len(nums))]
        # postfix = [0 for i in range(len(nums))]
        # ans = [0 for i in range(len(nums))]
        # for i in range(len(nums)):
        #     if i!=0: 
        #         tmp_list = nums.copy()
        #         tmp_list = tmp_list[:i]
        #         val = math.prod(tmp_list)
        #         prefix[i] = val
        #     else:
        #         prefix[i] = 1
        # for i in range(len(nums)):
        #     if i!=len(nums)-1 : 
        #         tmp_list = nums.copy()
        #         tmp_list = tmp_list[i+1:]
        #         val = math.prod(tmp_list)
        #         postfix[i] = val
        #     else:
        #         postfix[i] = 1
        # for i in range(len(nums)):
        #     ans[i] = postfix[i]*prefix[i]
        # return ans

