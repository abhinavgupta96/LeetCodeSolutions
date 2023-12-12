from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # this approach creates hashmap using default dict where key is element of nums list and the value is a list of indexes whose sum is the given target
        # hashmap = defaultdict(list)
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in nums and i != nums.index(diff):
        #         hashmap[nums[i]].append(i)
        #         hashmap[nums[i]].append(nums.index(diff))
        # return list(hashmap.values())[0]
        # Faster Solution
        # in this approach instead of storing the indexes of the occurence of a number, we just store the latest occurence which could be max of 2 only ans the problem is "two sum".
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            output = []
            diff = target - nums[i]
            if diff in hashmap and hashmap[diff]!=i:
                output.append(i)
                output.append(hashmap[diff])
                return output
        return []
            
        