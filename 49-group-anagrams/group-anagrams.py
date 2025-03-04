class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for word in strs:
            t = [0]*26
            for i in range(len(word)):
               t[ord(word[i]) - ord('a')] +=1
            t = tuple(t)
            hashMap[t].append(word)
        return list(hashMap.values())