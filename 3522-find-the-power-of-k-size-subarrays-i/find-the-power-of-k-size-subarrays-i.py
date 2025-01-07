class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        consecutiveCount = 1
        result = []
        l = 0

        for r in range(len(nums)):
            if r > 0 and nums[r-1]+1 == nums[r]:
                consecutiveCount+=1
            if r-l+1 > k:
                if nums[l+1] == nums[l]+1:
                    consecutiveCount-=1
                l+=1
            if r-l+1==k:
                result.append(nums[r] if consecutiveCount==k else -1)
        return result