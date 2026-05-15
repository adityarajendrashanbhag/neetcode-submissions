# Approach 2 :  Hashmaps
# TC: O(n) and SC: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i , num in enumerate(nums):
            subNum = target - num

            if subNum in visited:
                return [visited[subNum], i]
            
            visited[num] = i
        
        return [-1, -1]

        
        