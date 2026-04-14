class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n -1, -1, -1):
                p1, p2 = i + j, i + j + 1
                digit = int(num1[i]) * int(num2[j])
                total = res[p2] + digit

                res[p1] += total // 10
                res[p2] = total % 10
        
        res = "".join(map(str, res))
        return res if not res.startswith("0") else res[1:]