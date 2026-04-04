class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 

        prods = []
        prod = 1
        zeroPresent = 0
        [0,0,1,2]
        for n in nums:
            if n:
                prod *= n
            else: 
                zeroPresent += 1

        for n in nums:
            if n == 0 and zeroPresent <= 1:
                prods.append(prod)
            elif zeroPresent:
                prods.append(0)
            else:
                prods.append(prod//n)

        return prods
        