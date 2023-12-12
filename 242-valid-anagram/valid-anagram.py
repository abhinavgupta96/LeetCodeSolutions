class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            ##Solution 1 :
            ##sorts the two strings and compare them
            # return sorted(s)==sorted(t) 
            #---------#
            ## Solutuon 2 : 
            ##builds a hashmap for each of the string and compares them iteratively

            # hash_s = {} 
            # hash_t = {}
            # for i in list(s):
            #     if i not in hash_s:
            #         hash_s[i] = 1
            #     else:
            #         hash_s[i]+=1
            # for i in list(t):
            #     if i not in hash_t:
            #         hash_t[i] = 1
            #     else:
            #         hash_t[i]+=1
            # for i in hash_s:
            #     if i in hash_t and hash_t[i]==hash_s[i]:
            #         pass
            #     else:
            #         return False
            # return True


            return False

        ## Solution 3:
        # Builds hashmap and iterates over one of the string, then increments its count in the string, (.get method takes key, value as parameter where value is optional parameter to return the value if the key is not found in the dictionary)
        # in the end we just compare the two hashmaps 
        countS, countT = {}, {}
    
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT