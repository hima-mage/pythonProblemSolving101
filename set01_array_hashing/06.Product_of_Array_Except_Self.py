from typing import List


class Solution :
        def productExceptItself(self, nums: List[int]) -> List[int]:
            # make result array of sam
            result = [1] * len(nums)

            # prefix variable to store array elements multiplication before element occur
            prefix = 1
            # loop for each element in the nums array
            for i in range(len(nums)) :
                result[i] = prefix # make index with that element and make prefix as it's value
                prefix *= nums[i] # multiple every element into prefix to collect the value

            # postfix variable to store array elements multiplication after element occur
            postfix = 1
            # i will reverse loop the array
            for i in range(len(nums) -1 , -1 , -1 ):
                result[i] *= postfix
                postfix *= nums[i]

            return  result