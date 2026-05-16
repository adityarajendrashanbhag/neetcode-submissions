class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1

        freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

        freq = list(freq.keys())

        return freq[:k]
        