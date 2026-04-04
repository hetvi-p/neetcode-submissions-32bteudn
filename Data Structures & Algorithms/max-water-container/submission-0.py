class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxArea = 0
        l = 0
        r = len(heights) - 1
        length = len(heights) - 1

        while(l < r):
            
            maxArea = max(min(heights[l], heights[r]) * length, maxArea)

            if heights[l] > heights[r]:
                r -= 1
            else: 
                l += 1
            
            length -= 1
        
        return maxArea




        