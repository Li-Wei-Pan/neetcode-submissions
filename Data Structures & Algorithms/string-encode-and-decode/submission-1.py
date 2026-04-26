class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_result = ""
        for s in strs:
            counter = len(s)
            encoded_result += f"{counter}#{s}"
        #print(encoded_result)
        return encoded_result

    def decode(self, s: str) -> List[str]:
        result, i = [], 0


        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            # print('length', length)
            result.append(s[j + 1: j +1+ length])
            # print('result', result)
            i = j + 1 + length
        return result

