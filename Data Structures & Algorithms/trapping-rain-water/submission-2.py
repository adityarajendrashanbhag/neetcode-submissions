class Solution:
    def trap(self, height: List[int]) -> int:
        cnt = 0

        max_left = [0] * len(height)
        max_right = [0] * len(height)

        for i in range(1,len(height)):
            max_left[i] = max(max_left[i-1], height[i-1])

        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i+1])
        
        for i in range(len(height)):
            water = min(max_left[i], max_right[i]) - height[i]

            if water > 0:
                cnt += water
        
        return cnt

        