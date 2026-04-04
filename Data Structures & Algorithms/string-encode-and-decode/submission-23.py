class Solution:

    def encode(self, strs: List[str]) -> str:

        output = ""
        for s in strs:
            output += str(len(s))
            output += "#"
            output += s
        print(output)
        return output



    def decode(self, s: str) -> List[str]:

        res = []
        i = 0
        j = 0

        while i < len(s):
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res


""" 
        strs = []
        count = ""
        string = ""
        for c in s:
            if isinstance(count, int):
                string += c
                count -= 1
                if count == 0:
                    count = ""
            else:
                if string:
                    strs.append(string)
                    string = ""
                if c != "#":
                    count += c
                else:
                    count = int(count)
                    if count == 0:
                        strs.append(string)
                        count = ""


        if string:
            strs.append(string)
"""
