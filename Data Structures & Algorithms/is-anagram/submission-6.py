class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result1= {}
        result2= {}
        for i in s:
            if i not in result1:
                result1[i]= 1
            else:
                result1[i] += 1
        print(result1)
        print(f'---')
        for j in t:
            if j not in result2:
                result2[j]=1
            else:
                result2[j]+= 1
        print(result2)

        if result1 == result2:
            return True
        return False
        

        