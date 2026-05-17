class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for str in strs:
            result += f"{len(str)}#{str}"
        return result

    def decode(self, s: str) -> List[str]:
        start = 0
        end = 0
        strs = []
        while (start < len(s) and end < len(s)):
            if s[end] == "#":
                length = int(s[start:end])
                str = s[end + 1:end + 1 + length]
                strs.append(str)
                start = end + 1 + length
                end = end + 1 + length
            else:
                end += 1
        return strs
