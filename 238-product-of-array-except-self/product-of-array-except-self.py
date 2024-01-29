class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        The quickest approach satisfying the problem statement involves 2 passes over the nums list. For the first pass from the left, we use a local variable called as "left_product". In our ans array which we multiply the element over the current index value with that of the left_product, and then we update the value of left_product by multiplying it with the value from nums list at the same index. We do the same for the second pass where we approach the nums array from the back and keep updating the ans array.
        '''
        left_product = 1
        right_product = 1
        ans = [1]*len(nums)
        for i in range(len(nums)):
            ans[i]*= left_product
            left_product *=nums[i]

        for i in range(len(nums) - 1, -1 ,-1):
            ans[i]*=right_product
            right_product *=nums[i]
        return ans