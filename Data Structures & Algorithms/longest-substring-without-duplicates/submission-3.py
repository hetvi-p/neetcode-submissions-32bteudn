class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        longest = 0

        letters = {}

        for r in range(len(s)):

            while s[r] in letters and letters[s[r]] == 1:
                letters[s[l]] = 0
                l += 1
            
            longest = max(longest, len(s[l:r+1]))
            
            letters[s[r]] = 1

        return longest 
            




            


        
        