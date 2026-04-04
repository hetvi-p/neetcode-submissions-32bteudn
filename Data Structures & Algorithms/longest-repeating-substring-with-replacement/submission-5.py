class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        r = 0

        chars = {s[0]: 1}
        res = 0

        while r < len(s):

            max_freq = 0
            
            for key in chars:
                if chars[key] > max_freq:
                    max_freq = chars[key]

            if (r - l + 1) - max_freq <= k:
                if (r - l + 1) > res:
                    res = r - l + 1
                r += 1
                if r < len(s):
                    if s[r] in chars:
                        chars[s[r]] += 1
                    else:
                        chars[s[r]] = 1
            else:
                chars[s[l]] -= 1
                l += 1

        return res






        

        

