# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        groups = defaultdict(list)

        for s in strs:
            groups["".join(sorted(s))].append(s)

        return groups.values()