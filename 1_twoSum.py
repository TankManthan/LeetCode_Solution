from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return [lookup[complement], i]
            lookup[num] = i
            
obj = Solution()
result =obj.twoSum([1,2,3,4,5,6],11)  # it will return index of target
print(result)