class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums))
        suffix = [1] * (len(nums))

        for i in range(1, len(nums)):
            prefix[i] = (prefix[i-1] * nums[i-1])
        
        for i in range(len(nums)-1, 0, -1):
            suffix[i-1] = (suffix[i] * nums[i])
        
        result = [(prefix[i] * suffix[i]) for i in range(len(nums))]

        return result


        