from collections import defaultdict
from typing import List

"""
    O(m.n) solution 
    where 
    m number of the strings given
    n average length of string length

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)  # mapping charCount to list of anagrams

        for s in strs:
            count = [0] * 26  # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1

            result[tuple(count)].append(s)

        return result.values()

