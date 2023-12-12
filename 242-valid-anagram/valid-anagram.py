class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hash_s = {}
        hash_t = {}
        for i in s :
            if i not in hash_s:
                hash_s[i]=1
            else:
                hash_s[i]+=1
        for j in t : 
            if j not in hash_t:
                hash_t[j]=1
            else:
                hash_t[j]+=1
        # print(hash_s.keys())
        # print(hash_t.keys())
        if hash_t.keys() != hash_s.keys():
            return False
        for i in hash_s.keys():
            if hash_t[i] == hash_s[i]:
                pass
            else:
                return False
        return True
