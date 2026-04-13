class Solution:
    def getSum(self, a: int, b: int) -> int:
        max_int = 0x7FFFFFFF
        mask = 0xFFFFFFFF

        while b != 0:
            sum_no_carry = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a = sum_no_carry
            b = carry
        
        if a <= max_int:
            return a
        else:
            return ~(a ^ mask)