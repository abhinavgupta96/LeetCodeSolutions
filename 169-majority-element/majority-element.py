class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashDict = defaultdict(int)
        majority = len(nums)//2 + 1
        for i in nums:
            hashDict[i]+=1
            if hashDict[i]==majority:
                return i
            
        