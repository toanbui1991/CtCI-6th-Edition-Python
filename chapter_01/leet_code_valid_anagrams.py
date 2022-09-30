"""
problem: given two string s and t, check that t is an gram of
analyze: t anagrams of s if we just arrange character of s will have t
    one: if t is anagrams of s len(t) = len(s)
    two: if t is anagrams of s therefore Counter(t) = Counter(s). Or these two string is construct by the same set of element
"""
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)