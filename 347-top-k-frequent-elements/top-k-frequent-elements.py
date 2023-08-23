from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = defaultdict(list)
        for i in range(len(nums)):
            ans[nums[i]].append(nums[i])
        for i,j in ans.items():
            value = len(j)
            ans[i] = value
        sorted_value = sorted(ans, key= lambda x : ans[x], reverse= True)
        sorted_value = sorted_value[:k]
        return sorted_value
        