class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
        prev = [1]*len(nums)
        post = [1]*len(nums)
        for i in range(len(nums)):
            if i==0:
                prev[0] = 1
            else:
                prev[i] = prev[i-1]*nums[i-1]
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                post[i] = 1
            else:
                post[i] = post[i+1] * nums[i+1]
        for i in range(len(nums)):
            output[i] = prev[i]*post[i]
        return output
        