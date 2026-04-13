class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b:
            sum1 = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a = sum1
            b = carry
        
        return ~(a ^ mask) if a > max_int else a