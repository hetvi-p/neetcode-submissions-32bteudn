class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        key = {}
         
        for s in strs:
            
            lst = [0] * 26

            for c in s:
                ind = ord(c) - ord('a')
                lst[ind] += 1
            
            lst = tuple(lst)
            
            if lst in key:
                key[lst].append(s)
            else:
                key[lst] = [s]
        
        ret = []

        for k in key:
            ret.append(key[k])

        return ret

                    
