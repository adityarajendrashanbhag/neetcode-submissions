class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_sr = "".join([c for c in s if c.isalnum()]).lower()

        reverse_cleaned_sr = cleaned_sr[::-1]

        return cleaned_sr == reverse_cleaned_sr
        