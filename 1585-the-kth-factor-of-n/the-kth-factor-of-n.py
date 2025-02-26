class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # O(n) approach :
        # factorList = []
        # for i in range(1, n+1):
        #     if n%i==0:
        #         factorList.append(i)
        
        # if k <=len(factorList):
        #     return factorList[k-1]
        # else:
        #     return -1

        # O(n**0.5) approach
        factorCount = 0

        for potentialFactor in range(1, int(n**0.5)+1):
            if n %potentialFactor == 0:
                factorCount+=1
                if factorCount==k:
                    return potentialFactor
        if int(n**0.5)**2 == n:    
            potentialFactor = int(n**0.5)-1
        else:
            potentialFactor = int(n**0.5)

        for i in range(potentialFactor, 0, -1):
            if n%i == 0:
                factorCount+=1
                if factorCount==k:
                    return n//i
        return -1
