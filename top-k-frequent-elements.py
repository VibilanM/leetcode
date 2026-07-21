# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.

from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        count = dict(Counter(nums))
        sc = sorted(count.items(), key = lambda item: item[1], reverse=True)
        return [num for num, freq in sc[:k]]