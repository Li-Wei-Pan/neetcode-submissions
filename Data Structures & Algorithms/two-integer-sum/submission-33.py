class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for idx, num in enumerate(nums):
            dif = target - num
            # if num in mapping
            if dif in mapping:
                return [mapping[dif],idx ]
            #update hashmap
            mapping[num] = idx # {num: index}, we want index as result

        return  []
        