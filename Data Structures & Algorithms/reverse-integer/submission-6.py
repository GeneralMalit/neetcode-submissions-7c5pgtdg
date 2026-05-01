class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT, MIN_INT = 2 ** 31 - 1, -2 ** 31
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x:
            digit = x % 10
            x //= 10

            if res < MIN_INT or (res == MAX_INT // 10 and digit > 7):
                return 0

            res = (res * 10) + digit
        res *= sign
        return res if (MIN_INT <= res <= MAX_INT) else 0
