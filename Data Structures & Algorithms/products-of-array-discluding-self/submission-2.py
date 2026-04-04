class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 

        prods = []

        prefix = []
        p = 1
        for n in nums:
            prefix.append(p)
            p *= n

        suffix = []
        s = 1
        for n in nums[::-1]:
            suffix.append(s)
            s *= n
        #suffix = suffix[::-1]
    
        i = 0
        while i < len(nums):
            prods.append(prefix[i]*suffix[len(nums)-i-1])
            i += 1
        return prods




            
        