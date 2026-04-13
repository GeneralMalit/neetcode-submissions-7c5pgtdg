class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c_map = {}
        l = 0
        res = 0
        for r in range(len(s)):
            c = s[r]
            if c in c_map and c_map[c] >= l:
                print(f"{c} in c_map and {c_map[c]} > {l}")
                
                l = c_map[c] + 1
            c_map[c] = r 
            print(f"r = {r}, l ={l}")
            res = max(res, r - l + 1)

            
        return res
            

