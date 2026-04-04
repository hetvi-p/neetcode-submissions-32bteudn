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


        i = 0
        m = ""
        strs = []
        while i < len(s):
            j = i
            while s[j] != "#":
                print(s[j])
                m += s[j]
                j += 1
            m = int(m)
            strs.append(s[j+1:j+1+m])
            i = j+1+m
            m = ""
            
        return strs


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
