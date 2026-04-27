class Solution:

    def encode(self, strs: List[str]) -> str:
        result = "" 
        for s in strs:
            result += f"{len(s)}#{s}"
        return result  # "5#HELLO5#WORLD"


    def decode(self, s: str) -> List[str]:
        result, i = [], 0 #pointer

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1 # index of '#'
            length = int(s[i: j]) # s[0:1] get the length of str
            extract_word = s[j+1: j+1 + length]
            result.append(extract_word)
            i = j + 1 + length
            
        return result
