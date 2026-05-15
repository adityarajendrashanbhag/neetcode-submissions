# Approach 1 :  brute force method as it is fitting in time complexity 
# 10^6 < 10^8 so using O(n^2)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]
                
        return []
        