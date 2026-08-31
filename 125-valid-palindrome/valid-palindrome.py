class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(filter(str.isalnum, s)).lower()
        reversed_string = cleaned[::-1]
        if cleaned == reversed_string:
            return True
        return False