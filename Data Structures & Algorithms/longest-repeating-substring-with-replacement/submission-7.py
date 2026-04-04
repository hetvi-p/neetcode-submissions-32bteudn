class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        r = 0

        chars = {s[0]: 1}
        res = 0

        max_freq = 1

        while r < len(s):

            if (r - l + 1) - max_freq > k:
                chars[s[l]] -= 1
                l += 1
            else:
                res = max(res, (r - l + 1))
                r += 1
                if r < len(s):
                    chars[s[r]] = 1 + chars.get(s[r], 0)
                    max_freq = max(max_freq, chars[s[r]])
            print(r, l)

        return res






        

        

