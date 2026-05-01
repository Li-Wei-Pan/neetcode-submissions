class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst1 =  []
        lst2 = deque()
        s1 = s.split()
        
        for i in s:
            word = i.lower()
            if word.isalpha() or word.isnumeric():
                lst1.append(word)
                lst2.appendleft(word)
        print('lst1', lst1)
        print('---')
        print('lst2', lst2)
        lst2 = list(lst2)
        if lst1 == lst2:
            return True
        return False
            

            
        # print(lst1)