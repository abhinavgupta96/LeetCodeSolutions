from collections import defaultdict ##default dict gives a dict like object with a default value, here we use default values as empty list
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) ##initializing default dict
        for i in strs:
            temp = [0]*26 ##create an array with 26 elements, these represents characters a to z. So any string with same characters will end up with same temp list
            for c in i:
                val = ord(c) - ord("a") ##to figure out index of character in temp, we use ascii values and we subtract by a coz we need asbolute values
                temp[val]+=1
            res[tuple(temp)].append(i) ##dictonary in python donot allow list to be a key, so we convert our list into a tuple and append the value of string into the values section
        return res.values()
        