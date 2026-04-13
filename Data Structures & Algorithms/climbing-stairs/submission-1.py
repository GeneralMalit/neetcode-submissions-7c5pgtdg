class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        one = 1
        two = 1

        for i in range(2, 1 + n):
            curr = one + two
            one = two
            two = curr
        return two
