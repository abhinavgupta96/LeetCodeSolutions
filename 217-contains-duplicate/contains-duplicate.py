class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i]+=1
        for values in hash.values():
            if values > 1:
                return True
        