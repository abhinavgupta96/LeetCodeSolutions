class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #This approach uses a sorted value of a string as a key in a hashmap, if the key exists we add the string to the value of that key, in the end we return the list of values.
        ans = []
        hashmap = defaultdict(list)
        for i in range(len(strs)):
            val1 = sorted(strs[i])
            value = ""
            value = value.join(val1)
            hashmap[value].append(strs[i])
        for i in hashmap.values():
            ans.append(i)
        return ans