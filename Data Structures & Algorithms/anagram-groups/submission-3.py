class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grpAnagram = {}
        
        for i in range(len(strs)):
            grp = "".join(tuple(sorted(strs[i])))

            if grp not in grpAnagram:
                grpAnagram[grp] = []
            grpAnagram[grp].append(strs[i])

        return list(grpAnagram.values())


        