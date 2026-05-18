class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_list = sorted(set(nums))

        cnt = 1
        max_cnt = 1

        for i in range(len(nums_list) - 1):
            if (nums_list[i+1] - nums_list[i]) == 1:
                cnt += 1
                max_cnt = max(cnt, max_cnt)
            else:
                cnt = 1

        return max_cnt
        