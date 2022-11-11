class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ##neetcode approach, in the first pass, calculate prefix values for every index and update the output and in second pass, go from back and update output values with postfix value for each index
        output = [1]*len(nums)
        prefix = 1 ##take default prefix value, helps in dealing with edge case of the first element
        postfix = 1 ##take default prefix value, helps in dealing with edge case of the last element
        ##this is first pass 
        for i in range(len(nums)):
            output[i] = prefix ##update i index with prefix and then update prefix value
            prefix*=nums[i]
        ##this is second pass
        for i in range(len(nums)-1,-1,-1):
            output[i]*=postfix ##update output values by multiplying with postfix values
            postfix*=nums[i]
        return output
    ##my approach, takes more memory
    # prev = [1]*len(nums)
    # post = [1]*len(nums)
    # for i in range(len(nums)): ##calculates prev array
    #     if i==0:
    #         prev[0] = 1
    #     else:
    #         prev[i] = prev[i-1]*nums[i-1]
    # for i in range(len(nums)-1,-1,-1): ##calculates post array
    #     if i==len(nums)-1:
    #         post[i] = 1
    #     else:
    #         post[i] = post[i+1] * nums[i+1]
    # for i in range(len(nums)): ##gives output array by multiplying values from prev and post array
    #     output[i] = prev[i]*post[i]
        