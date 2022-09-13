from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n)
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # for every element in array make index in hash with counter of occurrence (element -> occurrence)
        for element in nums:
            count[element] = 1 + count.get(element, 0)  # use get to avoid error if that index not exist return 0

        # items(  Return the dictionary's key-value pairs:
        for element, occurrence in count.items():
            print(element , occurrence)
            freq[occurrence].append(element)
        print(freq)
        result = []
        # range(start, stop, step)
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
        return result


nums = [1, 2, 2, 1, 2, 4, 4, 4, 4 , 5]
target = 2
solutionClass = Solution()

print(solutionClass.topKFrequent(nums, target))
