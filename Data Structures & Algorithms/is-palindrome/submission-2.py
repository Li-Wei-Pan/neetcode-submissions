class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for word in s:
            if word.isalnum():
                new_str += word.lower()
        
        return new_str == new_str[::-1]