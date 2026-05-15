# Approach 2: 
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grpAnagram = defaultdict(list)

        for s in strs:
            grp = [0] * 26
            for c in s:
                grp[ord(c) - ord('a')] += 1
            grpAnagram[tuple(grp)].append(s)
        
        return list(grpAnagram.values())


        