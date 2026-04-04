class Solution:
    def findMin(self, nums: List[int]) -> int:

        low = 0
        high = len(nums) - 1
        
        mid = low + (high - low) // 2

        if nums[low] <= nums[high]:
            return nums[low]


        while low <= high:

            mid = low + (high - low) // 2

            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[low] > nums[mid] or nums[low] <= nums[high]:
                high = mid - 1
            else: 
                low = mid + 1
"""
[2, 3, 7, 9, 12]

[12, 2, 3, 7, 9]

if low is > mid OR high > low, then we take the first section
if 

[4, 7, 8, 9, 12, 2, 3]

[24, 25, 5, 6, 23]


"""





