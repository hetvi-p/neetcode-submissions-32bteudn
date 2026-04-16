class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res = 0
        present = defaultdict(int)

        for n in nums:
            if present[n] == 0:
                length = present[n-1] + present[n+1] + 1
                present[n] = length
                present[n - (present[n-1])] = length
                present[n + (present[n+1])] = length
                res = max(res, length)
        
        return res


        
            


