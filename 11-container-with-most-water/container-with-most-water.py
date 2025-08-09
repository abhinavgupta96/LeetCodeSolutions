class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxWater = 0

        while l!=r:
            if height[l] > height[r]:
                maxWater = max(maxWater, (r-l)*height[r])
                r-=1
            else:
                maxWater = max(maxWater, (r-l)*height[l])
                l+=1
        return maxWater