class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        final = []
        for num in nums:
            if num not in result:
                result[num] =0
            result[num] += 1
        
        sorted_dict = sorted(result.items(), key = lambda item: item[1], reverse = True )
        #print(sorted_dict)
        top_k_result = [i[0] for i in sorted_dict][:k]
        return top_k_result
    
        # return final