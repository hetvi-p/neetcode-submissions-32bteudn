class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        for i, n in enumerate(nums):

            if i > 0 and n == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while (left < right):

                if nums[left] + nums[right] + n == 0:
                    res.append([nums[left], nums[right], n])
                    right -= 1
                    left += 1
                    while(nums[left] == nums[left-1] and left < right):
                        left += 1
                    
                elif nums[left] + nums[right] + n > 0:
                    right -= 1
                else:
                    left += 1
                        
        return res
        