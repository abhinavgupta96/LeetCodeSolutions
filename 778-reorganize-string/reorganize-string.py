class Solution:
    def reorganizeString(self, s: str) -> str:
        strLength = len(s)
        counter = Counter(s)
        maxFreq = max(counter.values())

        if maxFreq > (strLength+1)//2:
            return ''
        index = 0
        reorganised = [0]*strLength
        for char, freq in counter.most_common():
            while freq : 
                reorganised[index] = char
                freq-=1
                index +=2
                if index >= strLength:
                    index=1
        return ''.join(reorganised)