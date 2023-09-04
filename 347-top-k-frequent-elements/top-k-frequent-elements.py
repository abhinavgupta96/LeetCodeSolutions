
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # my approach create a dict containing the number and their count
        # then use a sorted function to sort the dictionary based on values instead of keys
        # to do that we use a lambda function inside sorted(), where the key of the sorted func. is being passed  as the value of the dictionary
        # In the lambda function lambda x: ans[x], we are using the lambda function to sort the keys (x) of the ans dictionary based on their 
        # associated values (ans[x]). So, it doesn't return the keys explicitly but rather sorts them based on the values. 
        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = hash.get(nums[i], 0) + 1
        sorted_value = sorted(hash, key= lambda x : hash[x], reverse=True)
        return sorted_value[:k]
    
        # Neetcode approach is to create a hashmap of the dictionary with key as the number and the value as the count of its appreance in input
        # It then proceeds to create an array of arrays of size 1 more than the lenght of input
        # this freq array is used to store what numbers occur with what frequency, here the index refers to the count of appearance and the value at that index is a list of all the numbers that appear the same number of times i.e the index value.
        # we then traverse this freq array from back, adding the numbers in a final list until it reaches the required length
        
        # count = {}
        # freq = [[] for i in range(len(nums)+1)]
        # for i in nums:
        #     count[i] = 1 + count.get(i,0)
        
        # for number, count in count.items():
        #     freq[count].append(number)
        # res = []
        # for i in range(len(freq)-1,0,-1):
        #     for j in freq[i]:
        #         res.append(j)
        #         if len(res)==k:
        #             return res
        
