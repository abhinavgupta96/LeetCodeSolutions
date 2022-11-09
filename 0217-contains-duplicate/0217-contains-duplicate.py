class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        output=False
        # hash = {} create a dictionary and pass through all elements, with the value being the number of times that number appears in array
        # for i in range(len(nums)):
        #     if nums[i] not in hash:
        #         hash[nums[i]] = 1
        #     else:
        #         hash[nums[i]] +=1
        # for j in hash.values():
        #     if j>1:
        #         output = True
        #         return output
        hashset = set() ##this approach is where we create a set, set cannot contain duplicate values in python
        for n in nums:
            if n in hashset:
                output = True
                return output
            else:
                hashset.add(n)
        return output
    
        