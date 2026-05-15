class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        revisit = set()

        for i in nums:
            if i in revisit:
                return True
            
            revisit.add(i)
        
        return False

        