class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            x =  ''.join(sorted(s))
            result[x].append(s)
           
            
        return (list(result.values()))
            