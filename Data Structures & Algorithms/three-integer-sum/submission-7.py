# nums.sort() is O(1) space whereas sorted() create a new varibale to store them and sort them so O(n)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result_list = []

        for i in range(len(nums) - 1):
            left = i+1
            right = len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]:
                    continue

            while left < right:
                
                if (nums[i] + nums[left] + nums[right]) == 0:
                    result_list.append([nums[i], nums[left], nums[right]])

                    left +=1
                    right -=1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -=1
                
                elif (nums[i] + nums[left] + nums[right]) > 0:
                    right -= 1
                else:
                    left += 1
        
        return result_list