class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_c = 0

        left, right = 0, len(heights)-1

        while left < right:
            min_height = min(heights[left], heights[right])
            water_height = (min_height) * (right-left)
            max_c = max(max_c, water_height)

            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        
        return max_c
        