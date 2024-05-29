class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            digits = int(str(x)[1::][::-1])
            if 0-digits < -(2**31):
                return 0

            return 0-digits
        else:
            digits = int(str(x)[::-1])
            if digits > 2**31 - 1:
                return 0

            return digits