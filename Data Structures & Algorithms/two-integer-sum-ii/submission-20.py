class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            c1, c2 = numbers[l], numbers[r]
            total = c1 + c2
            if total == target:
                return [l + 1, r + 1]
            elif total < target:
                l += 1
            else:
                r -= 1
            

        return []