class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_target = {}
        output = []
        for i in range(len(nums)):
            hash_target[nums[i]] = i
        tmp = 0
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in hash_target and hash_target[tmp]!=i:
                return [i, hash_target[tmp]]
        return output
            
                
        