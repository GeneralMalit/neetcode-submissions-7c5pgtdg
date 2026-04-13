class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for r in range(1, len(s) + 1):
            for l in range(r):
                if dp[l] == True and s[l:r] in wordSet:
                    dp[r] = True
                    break

        return dp[len(s)]
