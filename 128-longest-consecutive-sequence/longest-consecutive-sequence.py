class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Cannot use sorting as it is O(n log(n))). While loop inside for loop does not necesarily mean O(n^2). 
        In this case we simply perform a lookup operation. 
        Logic is to find the start of each of the range that might exist in the given array, if we find that a number 1 greater than current 
        number is present in the set we continue to iterate, otherwise we move to the next number in the set.
        '''
        set_nums = set(nums)
        longest = 0
        
        for i in set_nums : 
            if i-1 not in set_nums : 
                y = i+1
                while y in set_nums:
                    y+=1
                sequence = y - i
                longest = max(longest,sequence)
        return longest
            