class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # store  {word : {letter list: frequency}}
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # from a to z 
            for c in s:
                #ascii value convertion
                count[ord(c)- ord("a")] += 1 #increment value if character is found
            res[tuple(count)].append(s) 

        return list(res.values())

            
