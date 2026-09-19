class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = "".join(filter(str.isalnum, s)).lower()
        for i in range(0, len(new)):
            if new[i] != new[len(new) - 1 - i]:
                return False
        return True