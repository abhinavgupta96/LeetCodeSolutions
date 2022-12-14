class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0 
        s = set(nums) ##create a set, helps dealing with duplicate values
        for num in nums:
            cur_longest = 1
            j = 1
            while num - j in s: ##check from current value, if values smaller than it exits
                s.remove(num - j) ##if value smaller exits, remove from set
                cur_longest = cur_longest + 1
                j =  j + 1
            j = 1
            while num + j in s: ##check if value greater than current exits, if they do remove it from the set
                s.remove(num + j)
                cur_longest = cur_longest + 1
                j = j + 1
            longest = max(longest, cur_longest) ##assign longest value as the max b/w longest sequence and current longest
        return longest
        
                
