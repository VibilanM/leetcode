# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

class Solution(object):
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0

        for i in numSet:
            if i-1 not in numSet:
                length = 1
                current = i

                while current+1 in numSet:
                    length += 1
                    current += 1

                longest = max(longest, length)
        
        return longest