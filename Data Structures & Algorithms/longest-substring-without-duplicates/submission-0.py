class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        l = 0
        max_length = 0
        for r in range(len(s)):
            char = s[r]
            if char in char_map and char_map[char] >= l:
                l = char_map[char] + 1
            
            char_map[char] = r
            max_length = max(max_length, r - l + 1)
        return max_length