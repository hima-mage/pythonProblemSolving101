class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()

        for n in nums:

            if n in hashset:
                return True

            hashset.add(n)

        return False


inputIntArray = [1, 2, 3, 33]
solutionClass = Solution();

print(solutionClass.containsDuplicate(inputIntArray))
