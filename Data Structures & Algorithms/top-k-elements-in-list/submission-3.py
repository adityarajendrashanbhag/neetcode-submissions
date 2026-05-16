class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:

            if i not in freq:
                freq[i] = 0
            freq[i] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for i,j in freq.items():
            buckets[j].append(i)
        
        result = []

        for i in buckets[::-1]:
            result.extend(i)
            if len(result) >= k:
                return result[:k]




        
        

        
        