class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ##my approach - thought we had to actually encode the string leading to O(n^2) solution
        # str = ""
        # for i in range(len(strs)):
        #     c = ""
        #     for j in range(len(strs[i])):
        #         c+=chr(ord(strs[i][j])+3)
        #     if i==len(strs)-1:
        #         str+=c
        #     else:
        #         str+=c+" "
        # return str
        ##neetcode approach - simply add an integer with a delimiter infront of each word in the input list
        c = ""
        for i in strs:
            c+=str(len(i)) + "#" + i
        return c
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ##my approach
        # str = s.split(sep=" ")
        # output = []
        # for i in str:
        #     c = ""
        #     for j in i:
        #         c+=chr(ord(j)-3)
        #     output.append(c)
        # return output
        
        ##neetcode approach - since input string will contain an integer followed by a delimiter, it will be easy to tell where a word ends
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!="#": ##since we take '#' as delimiter we need to find it
                j = j+1
            length = int(s[i:j]) ##after finding delimited we extract the lenght of the following word
            res.append(s[j + 1 : j + 1 + length]) ##once we know the length, we slice the string from index after delimter till the length of the word
            i = j + 1 + length
        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))