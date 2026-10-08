class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_mapping = [0]*27
        for letter in s:
            val = ord(letter) - 96
            print(val)
            s_mapping[val] += 1
        
        t_mapping = [0]*27
        for letter in t:
            val = ord(letter) -96
            t_mapping[val]+=1
        
        if s_mapping == t_mapping:
            return True
        return False