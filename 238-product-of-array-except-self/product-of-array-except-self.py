import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
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
        
        # Neetcode approach - have to understand it 
        res = [1] * (len(nums))

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

