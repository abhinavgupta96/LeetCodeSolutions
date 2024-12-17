class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashdict = defaultdict(list)
        for i in strs:
            hashkey = tuple(sorted(i))
            hashdict[hashkey].append(i)
        return list(hashdict.values())
        