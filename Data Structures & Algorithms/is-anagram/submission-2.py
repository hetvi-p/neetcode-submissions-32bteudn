class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        sd = {}
        td = {}

        for c in s:
            if c in sd:
                sd[c] += 1
            else:
                sd[c] = 1

        for c in t:
            if c in td:
                td[c] += 1
            else:
                td[c] = 1

        if td == sd:
            return True
        else:
            return False