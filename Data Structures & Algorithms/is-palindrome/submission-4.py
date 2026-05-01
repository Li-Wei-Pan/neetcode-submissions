class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers
        l,r = 0, len(s) -1
        while l < r:
            # if next str is not alphanum:
            while l < r and not self.isalphanum(s[l]):
                l +=1
            while r> l and not self.isalphanum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            
            l, r = l +1, r -1
        return True
            


        
    def isalphanum(self, s):
        return (ord('A')<= ord(s)<= ord('Z') or 
                ord('a')<= ord(s)<= ord('z') or
                ord('0')<= ord(s)<= ord('9'))