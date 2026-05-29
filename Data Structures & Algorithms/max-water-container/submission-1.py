class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_c = 0
        for i in range(len(heights) - 1):
            for j in range(i+1, len(heights)):
                min_height = min(heights[i], heights[j])
                water_height = (min_height) * (j-i)
                max_c = max(max_c, water_height)
        
        return max_c
        