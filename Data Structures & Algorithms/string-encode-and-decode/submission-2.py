class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += f"{i}aRU1ypdK9fswYAZ"
        return s
    def decode(self, s: str) -> List[str]:
        dec = s.split("aRU1ypdK9fswYAZ")
        dec.pop()
        return dec