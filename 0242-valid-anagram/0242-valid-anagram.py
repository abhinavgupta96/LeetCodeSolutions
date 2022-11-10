class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) == len(s):
            hash_s = {}
            hash_t = {}
            for i in list(s):
                if i not in hash_s:
                    hash_s[i] = 1
                else:
                    hash_s[i]+=1
            for i in list(t):
                if i not in hash_t:
                    hash_t[i] = 1
                else:
                    hash_t[i]+=1
            for i in hash_s:
                if i in hash_t and hash_t[i]==hash_s[i]:
                    pass
                else:
                    return False
            return True
        