class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(leftBias):
            l = 0
            r = len(nums)-1
            i = -1
            while l<=r:
                m = (l+r)//2
                if target > nums[m]:
                    l = m+1
                elif target < nums[m]:
                    r = m-1
                else:
                    i = m
                    if leftBias:
                        r = m-1
                    else:
                        l = m+1
            return i
        left = binarySearch(True)
        right = binarySearch(False)
        return [left, right]