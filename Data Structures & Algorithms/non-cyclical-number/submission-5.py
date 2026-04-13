class Solution:
    def isHappy(self, n: int) -> bool:
        def happy(number):
            total = 0
            while number > 0:
                digit = number % 10
                total += digit ** 2
                number //= 10

            return total
        
        slow, fast = n, happy(n)
        while slow != fast and fast != 0:
            slow = happy(slow)
            fast = happy(happy(fast))
        return fast == 1