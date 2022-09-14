"""
https://leetcode.com/problems/binary-search/

Given an array of integers nums which is sorted in ascending order,
 and an integer target, write a function to search target in nums.
  If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.


Notes :
    a) / operator aka classic division

    >>> 5/2
    2.5
    b) //operator aka floor division

    >>> 5//2
    2
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # set the left , right pointer -> which will used in Binary Search
        l, r = 0, len(nums) - 1

        # while the left < right -> there is still elements between -> else it's the only remain element
        while l <= r:
            # get middle Index which will used as start
            m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
            # if the middle element > the target element -> then go left side -> move right pointer to less than middle
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1