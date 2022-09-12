from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val : index
        """
        https://www.geeksforgeeks.org/enumerate-in-python/

        # changing index and printing separately
        """
        for i, element in enumerate(nums):

            diff = target - element

            if diff in prevMap:
                return [prevMap[diff], i]

            prevMap[element] = i

        return


nums = [1, 2, 3, 33 , 2, 4,5,6,7]
target =  35
solutionClass = Solution()

print(solutionClass.twoSum(nums, target))