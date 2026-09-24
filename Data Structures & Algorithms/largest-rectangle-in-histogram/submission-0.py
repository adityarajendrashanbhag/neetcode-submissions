class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i,h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left =  stack[-1] if stack else -1
                width = i - left - 1
                max_area = max(max_area, width * height)

            stack.append(i)

        while stack:
            height = heights[stack.pop()]
            left = stack[-1] if stack else -1
            width = len(heights) - left -1
            max_area = max(max_area, width * height)
        
        return max_area