from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_and_indices = {}
        for i, num in enumerate(nums):
            another = target - num
            if another in value_and_indices:
                return [i, value_and_indices[another]]
            value_and_indices[num] = i

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = Solution().twoSum(nums, target)

    print(result)
