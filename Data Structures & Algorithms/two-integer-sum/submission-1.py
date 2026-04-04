class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nd = {}
        for i in range(len(nums)):
            nd[target - nums[i]] = i

        for i in range(len(nums)):
            if nums[i] in nd and i != nd[nums[i]]:
                return [i,nd[nums[i]]]
        


        