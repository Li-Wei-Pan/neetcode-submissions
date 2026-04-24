class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for letter in s:
            if letter not in s_dict:
                s_dict[letter] =1
            else:
                s_dict[letter]+=1

        for letter in t:
            if letter not in t_dict:
                t_dict[letter] =1
            else:
                t_dict[letter]+=1
       
        print('s_dict', s_dict.items())
        print('t_dict', t_dict.items())

        if len(s) != len(t):
            return False
            
        for s_key, s_value in s_dict.items():
            if s_key not in t_dict or s_value != t_dict.get(s_key):
                return False
        return True
