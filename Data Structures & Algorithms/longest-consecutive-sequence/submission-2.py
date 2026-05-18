class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_list = sorted(set(nums))

        start = 0
        nxt = start + 1
        cnt = 1
        max_cnt = 1

        for i in range(len(nums_list) - 1):
            if (nums_list[nxt] - nums_list[start]) == 1:
                cnt += 1
                max_cnt = max(cnt, max_cnt)
            else:
                cnt = 1
            
            start += 1
            nxt += 1

        
        return max_cnt
        