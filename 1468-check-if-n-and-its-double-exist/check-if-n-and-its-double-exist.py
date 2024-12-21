class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # hashDict = defaultdict(int)
        # for n in range(len(arr)):
        #     hashDict[arr[n]] = n
        
        # for n in range(len(arr)):
        #     d = arr[n]*2
        #     if d in hashDict and hashDict[d]!=n:
        #         return True
        # return False
        # Uses Set instead of Hashmap
        seen = set()
        
        for val in arr:
            if val * 2 in seen or (val % 2 == 0 and val // 2 in seen):
                return True
            seen.add(val)
        
        return False
        