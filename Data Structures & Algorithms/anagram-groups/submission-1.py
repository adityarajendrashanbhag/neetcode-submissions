from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_list = defaultdict(list)

        for s in strs:
            alphabets_num = [0] * 26
            for c in s:
                alphabets_num[ord(c) - ord('a')] += 1

            group_list[tuple(alphabets_num)].append(s)
        
        return list(group_list.values())


        