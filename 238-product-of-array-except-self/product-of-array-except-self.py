class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = len(nums)*[1]   # create an array to store the result and initialize it with 1
        pre = len(nums)*[1]      # create an array to store prefix products and initialize it with 1
        post= len(nums)*[1]      # create an array to store suffix products and initialize it with 1
        pref, postf = 1 , 1      # initialize prefix and suffix products to 1
        
        # calculate prefix products
        for i in range(len(nums)):
            pre[i]= pref       # store the prefix product of nums[0:i] in pre[i]
            pref *= nums[i]    # update the prefix product by multiplying with the current number
            
        # calculate suffix products
        for i in range(len(nums)-1,-1,-1):
            post[i]= postf      # store the suffix product of nums[i+1:n] in post[i]
            postf *=nums[i]     # update the suffix product by multiplying with the current number
        
        result[0]= post[0]       # set result[0] to the suffix product of the last element
        result[len(nums)-1] = pre[len(nums)-1]   # set result[n-1] to the prefix product of the first element
        
        # calculate product of prefix and suffix values
        for i in range (1,len(nums)-1):
            result[i]=pre[i]*post[i]   # compute the product of prefix and suffix values
        
        return result     # return the final result array