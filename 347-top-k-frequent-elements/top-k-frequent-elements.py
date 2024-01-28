class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        hashset = {}
        for i in range(len(nums)):
            hashset[nums[i]] = hashset.get(nums[i], 0) + 1
        
        va = sorted(hashset.values(), reverse=True)[:k]
        for n in range(len(va)):
            for i,j in hashset.items():
                if va[n] == j and i not in ans:
                    ans.append(i)
                    break
            
        return ans
            