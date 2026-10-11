class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mappings = defaultdict(list)
        for word in strs:
            counter = [0]*27
            for letter in word.lower():
                counter[ord(letter) - ord('a')] +=1
            mappings[tuple(counter)].append(word)

        return list(mappings.values())
            
        