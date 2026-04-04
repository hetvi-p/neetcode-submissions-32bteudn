class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        for i, n in enumerate(nums):

            left = 0
            right = len(nums) - 1

            if left == i:
                left += 1
            if right == i:
                right -= 1

            while (left < right):

                if nums[left] + nums[right] + n == 0:
                    res.append([nums[left], nums[right], n])
                    right -= 1
                    left += 1
                if nums[left] + nums[right] + n > 0:
                    right -= 1
                if nums[left] + nums[right] + n < 0:
                    left += 1

                if left == i:
                    left += 1
                if right == i:
                    right -= 1

        seen = set()
        unique = []

        for g in res:
            key = tuple(sorted(g))   # sort so order doesn't matter
            if key not in seen:
                seen.add(key)
                unique.append(g)     # keep the original version

        return unique
        