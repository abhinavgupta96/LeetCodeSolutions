class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1>n2:
            return False
        
        s1Hash = [0]*26
        s2Hash = [0]*26

        for i in range(n1):
            s1Hash[ord(s1[i])-ord('a')]+=1
            s2Hash[ord(s2[i])-ord('a')]+=1
        
        if s1Hash == s2Hash:
            return True
        
        for i in range(n1,n2):
            s2Hash[ord(s2[i])-ord('a')]+=1
            s2Hash[ord(s2[i-n1])-ord('a')]-=1
            if s1Hash == s2Hash:
                return True
        return False
            