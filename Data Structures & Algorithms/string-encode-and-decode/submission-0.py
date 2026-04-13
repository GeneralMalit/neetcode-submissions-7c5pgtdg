class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for i in strs:
            out += f"{i}.-=-."
        return out
    def decode(self, s: str) -> List[str]:
        a = s.split(".-=-.")
        a.pop()
        return(a)
