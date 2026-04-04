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

        unique = []

        for g in res:
            key = sorted(g)
            if key not in unique:
                unique.append(key)

        return unique
        