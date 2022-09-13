"""

https://leetcode.com/problems/contains-duplicate/

check if the given array has Duplicates or not
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # create hashset to store each element in array while traverse
        hashset = set()
        # for each element in array
        for n in nums:
            # check if the element exist in hashset , if it's then it's duplicate
            if n in hashset:
                return True
            # else add it to hashset
            hashset.add(n)
        # no duplication return false
        return False


inputIntArray = [1, 2, 3, 33]
solutionClass = Solution()

print(solutionClass.containsDuplicate(inputIntArray))
