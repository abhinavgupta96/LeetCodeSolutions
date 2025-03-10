class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        step = 0
        while any(num>0 for num in nums) : 
            min_non_zero = min(num for num in nums if num>0)
            nums = [num-min_non_zero if num>0 else num for num in nums ]
            step+=1
        return step
