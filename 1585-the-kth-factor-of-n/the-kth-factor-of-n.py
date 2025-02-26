class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factorList = []

        for i in range(1, n+1):
            if n%i==0:
                factorList.append(i)
        
        if k <=len(factorList):
            return factorList[k-1]
        else:
            return -1