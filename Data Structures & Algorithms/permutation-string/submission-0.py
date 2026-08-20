class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r = 0,0
        s1_og_list = [s for s in s1]
        s1_list = s1_og_list[:]
        counter = 0
        target_len = len(s1)

        while r < len(s2):
            if s2[r] in s1_list:
                if counter == 0:
                    l = r
                s1_list.remove(s2[r])
                counter += 1

                if counter == target_len:
                    return True
                
                r += 1
            else:
                if counter > 0:
                    s1_list = s1_og_list[:]
                    counter = 0
                    r = l + 1
                else:
                    r += 1
        return False


            

        