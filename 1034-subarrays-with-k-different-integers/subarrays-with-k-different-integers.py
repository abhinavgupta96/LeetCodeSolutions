class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def counter(nums,k):
            countMap = {}
            count = 0
            l = 0

            for r in range(len(nums)):
                countMap[nums[r]] = 1 + countMap.get(nums[r],0)

                while len(countMap) > k:
                    countMap[nums[l]]-=1
                    if countMap[nums[l]]==0:
                        countMap.pop(nums[l])
                    l+=1
                count+= r-l+1
            return count
        return counter(nums, k) - counter(nums,k-1)