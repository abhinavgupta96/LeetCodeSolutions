from bisect import bisect_left
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        '''
        Two pointer approach
        '''
        # nums.sort()
        # n = len(nums)
        # count = 0

        # for i in range(n):
        #     low, high = i+1, n-1
        #     while low<=high:
        #         if nums[i] + nums[low] < lower:
        #             low+=1
        #         elif nums[i] + nums[high] > upper:
        #             high-=1
        #         else:
        #             count+=(high - low)+1
        #             break
        # return count
        '''
        Sorting plus Binary Search approach
        '''
        nums.sort()
        count = 0
        for i, num in enumerate(nums):
            left_index = bisect_left(nums, lower-num, lo=i+1)
            right_index = bisect_left(nums, upper-num+1, lo=i+1)
            count += right_index - left_index
        return count
