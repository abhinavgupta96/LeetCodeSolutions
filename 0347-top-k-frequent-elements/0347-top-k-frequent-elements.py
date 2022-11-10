class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ##my solution
        # output = []
        # hash_map = {}
        # for i in nums: #build a hashmap of numbers and their counts
        #     if i not in hash_map:
        #         hash_map[i] = 1
        #     else:
        #         hash_map[i]+=1
        # temp = sorted(hash_map.values(),reverse=True) #sort the values of hashmap in reverse and slice it according to k giving the top k frequency
        # temp = temp[:k]
        # for i in temp:
        #     for j in hash_map:
        #         if hash_map[j]==i and j not in output: ##add number in output
        #             output.append(j)
        # return output
        
        ##neetcode solution employs a version of bucket sort
        hash_map = {}
        for i in nums: #build a hashmap of numbers and their counts
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i]+=1
        freq = [[] for i in range(len(nums)+1)] ##build a list of length more than the length of input list
        
        for n,c in hash_map.items():
            freq[c].append(n) ##basically we are adding list of numbers that appear a number of times at that index in freq list. So if 1  and 2 appear 3 times, we will add [1,2] at index 3 of freq
        res = []
        for i in range(len(freq)-1,0,-1): ##traversing freq list from back, since that will give us the most frequent elements in decreasing order
            for n in freq[i]: ##accessing the list of elements at that index
                res.append(n)
                if len(res)==k: ##stopping once length of output list is same as k
                    return res