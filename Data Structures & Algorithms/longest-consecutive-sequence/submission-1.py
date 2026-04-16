class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        present = set()
        for n in nums:
            present.add(n)

        res = 0

        for n in nums:
            count = 1

            i = n
            while (i + 1) in present:
                count += 1
                i += 1

            res = max(res, count)
        
        return res
            
            


