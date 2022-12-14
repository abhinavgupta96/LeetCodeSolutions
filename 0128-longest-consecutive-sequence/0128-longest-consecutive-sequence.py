class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0 
        s = set(nums)
        for num in nums:
            cur_longest = 1
            j = 1
            while num - j in s: 
                s.remove(num - j)
                cur_longest = cur_longest + 1
                j =  j + 1
            j = 1
            while num + j in s: 
                s.remove(num + j)
                cur_longest = cur_longest + 1
                j = j + 1
            longest = max(longest, cur_longest)
        return longest
        
                