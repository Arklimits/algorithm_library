class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x < 10:
            return True

        digits = str(x)
        length = len(digits)
        for i in range(length // 2):
            if digits[i] != digits[length-i-1]:
                return False

        return True