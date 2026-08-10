# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)