class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # implemented hash map
        hashmap = {} # value : index

        for ind, value in enumerate(nums):
            difference = target - value
            if difference in hashmap:
                return [hashmap[difference], ind]

            # update hashmap if not found
            hashmap[value] = ind
        return 