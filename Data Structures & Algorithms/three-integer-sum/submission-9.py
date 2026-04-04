class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        for i, n in enumerate(nums):

            left = i + 1
            right = len(nums) - 1

            while (left < right):

                if nums[left] + nums[right] + n == 0:
                    res.append((nums[left], nums[right], n))
                    right -= 1
                    left += 1
                if nums[left] + nums[right] + n > 0:
                    right -= 1
                if nums[left] + nums[right] + n < 0:
                    left += 1


        res = list(set(res))

        return [list(r) for r in res]
        