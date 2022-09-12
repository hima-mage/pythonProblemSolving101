"""
https://leetcode.com/problems/valid-anagram/submissions/

this will check if the string has same number of chars in it and same duplication
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #  easy solution is using Counter(s) == Counter(t) which is hashmap in python that count the char for u

        #  check if the length is not equal so it's false
        if len(s) != len(t):
            return False

        # setting hashmap to trace each char in each string
        countS, countT = {}, {}

        for i in range(len(s)):
            # i used get here to prenet error if the element not exist in hashmape countS
            countS[s[i]] = 1 + countS.get(s[i], 0) # setting each element counter , if it's no exist return 0 increment
            countT[t[i]] = 1 + countT.get(t[i], 0) # setting each element counter , if it's no exist return 0 increment

        #  check each char in first hashmap
        for c in countS:
            # i used get here to prenet error if the element not exist in hashmape countS
            # if that char not has same duplication in second hashmap return false
            if countS[c] != countT.get(c, 0):
                return False

        #  else return true
        return True


s = "anagramc"
t = "nagaram"
solutionClass = Solution()

print(solutionClass.isAnagram(s, t))
