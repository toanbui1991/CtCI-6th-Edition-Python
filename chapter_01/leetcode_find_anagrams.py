from collections import Counter
from typing import List

"""
problem: given two string s and p. find all start position of of s which start of an anagram of p.
analyze: we need to loop throug a list using window
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        reference = Counter(p)
        window = len(p)
        result_list = []

        for i in range(len(s) - window +1): #loop trough array with fix window len(s) - window + 1
            #construct of update counter (do not create new counter every step)
            if i == 0:
                candidate = Counter(s[:len(p)])
            else:
                candidate[s[i-1]] -= 1 #remove previous e which is outside window
                candidate[s[i+window-1]] += 1 #add new element which is inside window. i+window-1
            if candidate[s[i]] == 0:
                del candidate[s[i]] 
            #check two counter, if True append   
            if candidate == reference:
                result_list.append(i)
            #move to the next
            i += 1

            
        return result_list