class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        max_abs = 0
        for x in nums:
            if abs(x) > max_abs:
                max_abs = abs(x)

        arr = [[None, None] for _ in range(max_abs + 1)]
        for n in nums:
            if n >= 0:
                if arr[n][0] is None:
                    arr[n][0] = n
                else:
                    return True
            else: 
                if arr[-n][1] is None: 
                    arr[-n][1] = n 
                else: 
                    return True

        return False


        