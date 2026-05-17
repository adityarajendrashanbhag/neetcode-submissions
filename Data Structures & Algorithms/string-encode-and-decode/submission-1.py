"""
Step 1 — Restate the problem

"So I need to encode a list of strings into one single string, and then decode it back to the exact same list"

Step 2 — Identify the challenge

"The naive approach would be joining with a separator like #, but the problem says strings can contain any ASCII character — so any separator I pick could appear inside a string and confuse the decoder"

Step 3 — State your approach

"So instead of a separator, I'll use length prefixing — before each string I write its length followed by a #, so the decoder knows exactly how many characters to read and never has to guess where a string ends"

Step 4 — Give a quick example

"["Hello", "World"] becomes 5#Hello5#World — the decoder reads 5, jumps exactly 5 characters, gets Hello, then repeats"

Step 5 — Mention complexity

"This is O(n) time and space since we touch every character exactly once"


The key is step 2 — always explain why the obvious approach fails before jumping to your solution. It shows you actually thought about the problem and didn't just memorize the answer.

"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = s.index('#', i) # 1
            prefix_length = int(s[i:j]) # 2
            res.append(s[j+1: j+1+prefix_length])
            i = j+1+prefix_length

        return res
