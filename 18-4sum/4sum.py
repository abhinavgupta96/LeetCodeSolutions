class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums)<4:
            return []
        
        result = []
        nums.sort()
        numLen = len(nums)
        for i in range(numLen-3):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            for j in range(i+1, numLen-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                left = j+1
                right = numLen-1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total < target:
                        left+=1
                    
                    elif total > target:
                        right-=1
                    else:
                        temp = [nums[i],nums[j],nums[left],nums[right]]
                        left+=1
                        right-=1
                        result.append(temp)
                        while left < right and nums[left]==nums[left-1]:
                            left+=1
                        
                        while left < right and nums[right]==nums[right+1]:
                            right-=1
        return result
        
                

