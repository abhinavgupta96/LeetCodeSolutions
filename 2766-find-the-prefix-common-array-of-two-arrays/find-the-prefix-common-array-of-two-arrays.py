class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        idx_dict = {val : idx for idx,val in enumerate(B)}

        result = [0]*n

        for i in range(len(A)):
            idx = idx_dict[A[i]]
            max_idx = max(idx, i)
            result[max_idx]+=1
            if i > 0:
                result[i]+= result[i-1]
        return result