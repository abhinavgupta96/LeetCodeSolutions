class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        s = list(s)
        sum = 0
        for i in range(len(s)):
            if i==len(s)-1 or hashmap[s[i]]>=hashmap[s[i+1]]:
                sum+=hashmap[s[i]]
            else:
                sum-=hashmap[s[i]]
            
        return sum
            
            
        