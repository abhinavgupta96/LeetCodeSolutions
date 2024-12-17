class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashdict = defaultdict(list)
        # for i in strs:
        #     hashkey = tuple(sorted(i))
        #     hashdict[hashkey].append(i)
        # return list(hashdict.values())
        hashdict = defaultdict(list)
        
        for word in strs:
            t = [0]*26
            for c in word:
                t[ord(c) - ord('a')]+=1
            key = tuple(t)
            hashdict[key].append(word)
        return list(hashdict.values())

                
        