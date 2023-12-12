from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(list)
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums and i != nums.index(diff):
                hashmap[nums[i]].append(i)
                hashmap[nums[i]].append(nums.index(diff))
        return list(hashmap.values())[0]
        