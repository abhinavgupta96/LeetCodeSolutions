class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_dict = Counter(nums)

        for i, j in nums_dict.items():
            if j==1:
                return i