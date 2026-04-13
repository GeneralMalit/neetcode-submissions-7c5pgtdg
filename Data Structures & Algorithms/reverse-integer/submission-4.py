class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31

        sign = -1 if x < 0 else 1

        x = abs(x)
        res = 0
        while x:
            digit = x % 10
            x //= 10

            if res > MAX_INT or (res == MAX_INT and digit > 7):
                return 0

            res = (res * 10) + digit
        res = sign * res
        return res if (res > MIN_INT and res < MAX_INT) else 0