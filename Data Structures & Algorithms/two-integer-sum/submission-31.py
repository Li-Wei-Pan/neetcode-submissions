class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target - cur = remaining nr
        record = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in record:
                return [record[diff], idx]
            record[num] = idx


        return []
                
            

        