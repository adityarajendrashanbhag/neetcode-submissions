class Solution:
    def trap(self, height: List[int]) -> int:
        cnt = 0
        max_left = [max(height[0:i]) if i > 0 else 0 for i in range(len(height))]
        max_right = [max(height[i+1:]) if i < len(height) - 1 else 0 for i in range(len(height))]

        for i in range(len(height)):
            water = min(max_left[i], max_right[i]) - height[i]

            if water > 0:
                cnt += water
        
        return cnt

        