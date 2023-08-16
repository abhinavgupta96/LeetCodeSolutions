class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
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
            