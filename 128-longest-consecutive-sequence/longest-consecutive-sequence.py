class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Cannot use sorting as it is O(n log(n))). While loop inside for loop does not necesarily mean O(n^2). 
        In this case we simply perform a lookup operation. 
        Logic is to find the start of each of the range that might exist in the given array, if we find that a number 1 greater than current 
        number is present in the set we continue to iterate, otherwise we move to the next number in the set.
        '''
        # set_nums = set(nums)
        # longest = 0
        # for i in nums:
        #     length = 0
        #     while i + length in nums : 
        #         length+=1
        #         longest = max(longest,length)
        # return longest
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
            longest = max(longest, cur_longest)
        return longest
            