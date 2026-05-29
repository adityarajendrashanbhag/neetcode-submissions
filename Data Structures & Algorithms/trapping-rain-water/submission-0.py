class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        
        for i in range(len(height)):
            max_left = max(height[0:i]) if i > 0 else 0
            max_right = max(height[i+1:]) if (i < len(height) - 1) else 0

            water = min(max_left, max_right) - height[i]

            if water > 0:
                total += water
        
        return total
        