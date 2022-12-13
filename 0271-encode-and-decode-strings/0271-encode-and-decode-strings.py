class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        str = ""
        for i in range(len(strs)):
            c = ""
            for j in range(len(strs[i])):
                c+=chr(ord(strs[i][j])+3)
            if i==len(strs)-1:
                str+=c
            else:
                str+=c+" "
        return str
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        str = s.split(sep=" ")
        output = []
        for i in str:
            c = ""
            for j in i:
                c+=chr(ord(j)-3)
            output.append(c)
        return output
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))