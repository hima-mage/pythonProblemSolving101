"""
https://leetcode.com/problems/search-a-2d-matrix/


Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.



"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # get number of rows and cols ->  [i][j]
        ROWS, COLS = len(matrix), len(matrix[0])

        # here the two pointer will be first row - last cols
        top, bot = 0, ROWS - 1
        # if the top <= bot keep the iterate
        while top <= bot:
            # 0 + 4 -> get the second row
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False