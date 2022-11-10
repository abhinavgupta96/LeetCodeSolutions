class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) == len(s):
            # return sorted(s)==sorted(t) sorts the two strings and compare them
            hash_s = {} #build a hashmap of each string and then compare them
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
        
