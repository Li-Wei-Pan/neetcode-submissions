class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,1
        result = []
        while r < len(numbers):
            num1 = numbers[l]
            for i in range(r, len(numbers)):
                num2 = numbers[i]
                if num1 + num2 == target:
                    result.append(l+1)
                    result.append(i +1)
                    return result
                    break
            l,r = l+1, r+1

        return []