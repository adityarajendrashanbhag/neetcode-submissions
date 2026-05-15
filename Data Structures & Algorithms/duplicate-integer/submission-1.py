class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_num = set()
        for i in nums:
            if i in seen_num:
                return True
            seen_num.add(i)
        return False
            

        