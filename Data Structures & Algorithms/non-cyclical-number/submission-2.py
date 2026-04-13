class Solution:
    def isHappy(self, n: int) -> bool:
        def happy(n):
            total = 0
            while n > 0:
                digit = n % 10
                total += digit ** 2
                n //= 10
            return total
        slow, fast = n, happy(n)
        while slow != fast and fast != 0:
            slow = happy(slow)
            fast = happy(happy(fast))
        return fast == 1