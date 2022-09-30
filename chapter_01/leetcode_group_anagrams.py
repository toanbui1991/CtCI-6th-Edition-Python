from collections import defaultdict
"""
problem: given a list of string group anagram together.
problem reference: https://leetcode.com/problems/group-anagrams/
solution:
    one: if two string is anagrams then sorted(s1) == sorted(s2)
    #using defaultdict(list)
"""

def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        a = defaultdict(list) #if do not have key return empty dict
        for s in strs:
            a[tuple(sorted(s))].append(s) #each time it will return a list to append new element
        return a.values()