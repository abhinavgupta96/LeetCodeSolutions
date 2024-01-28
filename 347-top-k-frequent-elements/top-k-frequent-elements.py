class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''Slower approach as here we build a dictionary with elements as keys and its occurence as values. Since dictionaries are unordered there is no straightfwd way to sort them. This approach takes the list of values and sorts them in descending order in the length of 'k'. We then use nested for loops to iterate over the list of values and find the key which has the value '''

        # ans = []
        # hashset = {}
        # for i in range(len(nums)):
        #     hashset[nums[i]] = hashset.get(nums[i], 0) + 1
        
        # va = sorted(hashset.values(), reverse=True)[:k]
        # for n in range(len(va)):
        #     for i,j in hashset.items():
        #         if va[n] == j and i not in ans:
        #             ans.append(i)
        #             break
            
        # return ans
        '''
        A quicker approach, here we first use a default dict to build a hashmap with value as key and list of its appearances as its value. We then replace this list of apperance with its len. Now we use sorted function and to sort the dictionary in descending order based of values and return to us the keys.
        '''
        ans = defaultdict(list)
        for i in range(len(nums)):
            ans[nums[i]].append(nums[i])
        for i,j in ans.items():
            value = len(j)
            ans[i] = value
        
        ''' 
        The lambda function takes a key x (which is a number in this case). It returns the frequency of that key from the ans dictionary (i.e., how many times that number appears in the list). 
        For each number (x), tell me how many times it appears in the list according to the ans dictionary." This information is then used by the sorted() function to sort the numbers based on their frequencies.
        '''

        sorted_value = sorted(ans, key= lambda x : ans[x], reverse= True)
        
        sorted_value = sorted_value[:k]
        return sorted_value
            