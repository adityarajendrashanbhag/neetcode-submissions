class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_list = set(nums)

        start = 0
        rec = 1
        cnt = 1
        max_count = 1
        
        for i in nums_list:
            if (i-1) not in nums_list:
                cnt = 1
                rec = 1
                while (i + rec) in nums_list:
                    cnt += 1
                    rec += 1
                max_count = max(max_count, cnt)

        return max_count