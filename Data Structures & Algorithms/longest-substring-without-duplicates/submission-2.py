class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        if len(s) == 0:
            return 0
        l = 0
        r = 1
        longest = 1

        letters = {}
        letters[s[l]] = 1


        while r < len(s):

            if (s[r] in letters and letters[s[r]] == 1):
                while s[l] != s[r]:
                    letters[s[l]] = 0
                    l += 1
                l += 1
            
            longest = max(longest, len(s[l:r+1]))
            
            letters[s[r]] = 1
            r += 1

        return longest 
            




            


        
        